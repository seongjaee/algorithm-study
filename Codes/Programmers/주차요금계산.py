import math

def solution(fees, records):
    basic_time, basic_fee, unit_time, unit_fee = fees

    def get_time(in_time, out_time="23:59"):
        sh, sm = map(int, in_time.split(':'))
        eh, em = map(int, out_time.split(':'))
        return (eh - sh) * 60 + (em - sm)

    def get_fee(time):
        return basic_fee + math.ceil(max(0, time - basic_time) / unit_time) * unit_fee
        
    total_time_dict = {} # 차량번호: 누적 시간
    time_dict = {} # 차량번호: 입/출 시각

    for record in records:
        time, car, _ = record.split(' ')
        if car in time_dict:
            t = get_time(time_dict.pop(car), time)
            total_time_dict[car] = total_time_dict.get(car, 0) + t
        else:
            time_dict[car] = time


    for car, time in time_dict.items():
        t = get_time(time_dict[car])
        total_time_dict[car] = total_time_dict.get(car, 0) + t

    sorted_car = sorted(total_time_dict.keys())

    answer = []
    for car in sorted_car:
        answer.append(get_fee(total_time_dict[car]))

    return answer


print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))