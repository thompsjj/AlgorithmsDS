# python3

from collections import deque

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = start_time

from collections import deque

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = int(arrival_time)
        self.process_time = int(process_time)

class Response:
    def __init__(self, dropped, start_time):
        self.dropped = dropped
        self.start_time = int(start_time)

class Buffer:
    def __init__(self, size):
        self.size = int(size)
        self.finish_time_ = deque()

    def flush_jobs(self, reference_time):
        
        # this method flushes the buffer up to the reference time
        
        if len(self.finish_time_):
            while len(self.finish_time_):
                current_job = self.finish_time_[0]
 
                if current_job > reference_time:
                    break
            
                self.finish_time_.popleft()

        return
            
    def get_finish_time(self):
        if len(self.finish_time_):
            return self.finish_time_[-1]
        else:
            return None
        
    def Process(self, request):
        
        self.flush_jobs(request.arrival_time) # flush all jobs that should have been finished by now
        soonest_finish = self.get_finish_time() # get the current soonest finish
        N = len(self.finish_time_)

        if N:    
            if request.arrival_time >= soonest_finish: # all jobs should be complete to here

                self.finish_time_.append(request.arrival_time+request.process_time)
                
                return Response(False, request.arrival_time)
            
            else:
                if N < self.size: # if there is space remaining in the buffer, append to the buffer
                    
                    self.finish_time_.append(soonest_finish+request.process_time)
                    
                    return Response(False, soonest_finish)
                else:
                    # in this case the buffer size has been exceeded
                    return Response(True, -1)                      
    
        else:
            # in the case where the buffer is empty
            self.finish_time_.append(request.arrival_time+request.process_time)
            return Response(False, request.arrival_time)
        
def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ReadRequestsFromFile(filename):
    requests = []
    with open(filename, "r") as f:
        lines = f.readlines()
        size, counts = lines[0].split(' ')       
        print("loading ", size, "line buffer, processing", counts, "requests")
        for l in lines[1:]:
            arrival_time, process_time = l.split(' ')
            requests.append(Request(arrival_time, process_time))            
    return int(size), int(counts), requests
            
            
def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)


def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)

    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)

    PrintResponses(responses)