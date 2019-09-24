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
        load = 0
        for quest in request:
            if load == 0:
                load += 1
                self.finish_time.append(quest[1])
                return quest[0]



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
