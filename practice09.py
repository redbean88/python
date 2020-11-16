try:
    print("나누기 전용 계산기 입니다.")
    nums = []

    nums.append(int(input("첫 번째 숫자를 입력하세요")))
    nums.append(int(input("두 번째 숫자를 입력하세요")))
    nums.append(int(nums[0]/nums[1]))
    print("{0}/{1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err: # 최상위 부모
    print("알수 없는 에러가 발생하였습니다.")
    print(err)


# 에러 발생 강제

try:
    print("한 자리 숫자 나누기 전용 계산기힙니다.")
    num1 = int(input("첫 번째 숫자를 입력 하세요 :"))
    num2 = int(input("두 번째 숫자를 입력 하세요 :"))
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print("{0}/{1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다.")

# 커스텀 에러
class BigNumberError(Exception):
    # pass
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기힙니다.")
    num1 = int(input("첫 번째 숫자를 입력 하세요 :"))
    num2 = int(input("두 번째 숫자를 입력 하세요 :"))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력 값 : {0} , {1}".format(num1 , num2))
    print("{0}/{1} = {2}".format(num1, num2, int(num1/num2)))
except BigNumberError as err:
    print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력 하세요")
    print(err)

# finally

try:
    print("한 자리 숫자 나누기 전용 계산기힙니다.")
    num1 = int(input("첫 번째 숫자를 입력 하세요 :"))
    num2 = int(input("두 번째 숫자를 입력 하세요 :"))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력 값 : {0} , {1}".format(num1, num2))
    print("{0}/{1} = {2}".format(num1, num2, int(num1 / num2)))
except BigNumberError as err:
    print("잘못된 값을 입력하였습니다. 한자리 숫자만 입력 하세요")
    print(err)
finally:
    print("계산이 완료 되었습니다.")