from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from .models import TwoSumRequest
from .pagination import PaginationHandlerMixin
from .serializers import TwoSumRequestSerializer


class BasicPagination(PageNumberPagination):
    page_size_query_param = 'limit'


class TwoSumRequestList(APIView, PaginationHandlerMixin):
    pagination_class = BasicPagination
    serializer_class = TwoSumRequestSerializer

    def get(self, request):
        two_sum_requests = TwoSumRequest.objects.all()
        page = self.paginate_queryset(two_sum_requests)

        if page is not None:
            serializer = self.get_paginated_response(
                self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(two_sum_requests, many=True)

        return Response({"two sum requests": serializer.data})

    def post(self, request):
        two_sum_request = request.data.get('input')

        # Create a two_sum_request from the above data
        serializer = self.serializer_class(data=two_sum_request)

        if not serializer.is_valid(raise_exception=True):
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            input_validation(
                    serializer.validated_data['nums'],
                    serializer.validated_data['target']
            )

            output = two_sum(
                serializer.validated_data['nums'],
                serializer.validated_data['target']
            )
            serializer.save()

            return Response(
                {"output": output},
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response({"message": f"{e}"},
                            status=status.HTTP_400_BAD_REQUEST)


class TwoSumRequestDetail(APIView):
    @staticmethod
    def get(request, pk):
        # Get object with this pk
        two_sum_request = get_object_or_404(TwoSumRequest.objects.all(), pk=pk)

        return Response({
            f"Two sum request with id `{pk}`": f"{two_sum_request}"
        })

    @staticmethod
    def delete(request, pk):
        # Get object with this pk
        two_sum_request = get_object_or_404(TwoSumRequest.objects.all(), pk=pk)
        two_sum_request.delete()

        return Response({
            "message": f"Two sum request with id `{pk}` has been deleted."
        })


def input_validation(nums: list, target: int):
    """Check if input values follow the constraints:
    2 <= nums.length <= 10^4
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9
    Raise the exception with custom message if not
    """
    try:
        nums_length = len(nums)
    except TypeError as type_error:
        raise Exception("Parameter 'nums' should be a list with "
                        "integer numbers") from type_error

    if not 2 <= nums_length <= 10**4:
        raise Exception("Length of parameter 'nums' should be more "
                        "than 2 and less than 10^4")

    if len(list(filter(
            lambda num: -10**9 <= num <= 10**9, nums))) != nums_length:
        raise Exception("Every number in parameter 'nums' should "
                        "be more than -10^9 and less than 10^9")

    if not -10 ** 9 <= target <= 10 ** 9:
        raise Exception("Parameter 'target' should be more than -10^9 and "
                        "less than 10^9")


def two_sum(nums: list, target: int) -> list:
    """Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target
    or an error if we cannot find the sum of numbers for a given target
    """
    index = 0
    nums_and_indexes = {}

    for num in nums:
        if target - num in nums_and_indexes:
            return [nums_and_indexes[target-num], index]
        nums_and_indexes[num] = index
        index += 1

    raise Exception("Cannot find the sum of numbers for a given target")
