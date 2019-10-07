# python3

import collections
from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = collections.deque()

    def process(self, request):
        # write your code here

        while len(self.finish_time) > 0 and request.arrived_at >= self.finish_time[0]:
            self.finish_time.popleft()
        if len(self.finish_time) < self.size:
            if len(self.finish_time) == 0:
                start = request.arrived_at
            else:
                if request.arrived_at <= self.finish_time[-1]:
                    start = self.finish_time[-1]
                else:
                    start = request.arrived_at
            self.finish_time.append(start + request.time_to_process)
            return Response(False, start)
        else:
            return Response(True, -1)

        # return Response(False, -1)


def process_requests(requests, buffer):
    if buffer == 0 and len(requests) > 0:
        return -1
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
