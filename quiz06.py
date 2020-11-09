# 문제 ) 표준 체중을 구하는 프로그램을 작성하시오

# * 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
#  남자 : 키(m) * 키(m) * 22
#  여자 : 키(m) * 키(m) * 21

# 조건 1 : 표준 체중은 별도의 함수 내에서 계산
#         * 함수명 : std_weight
#         * 전달값 : 키(height) , 성별(gender)
# 조건 2 : 표준 체중은 소수점 둘째자리까지 표시

# (예시)
# 키 175cm 남자의 표준 체중은 67.38kg입니다

def BMI(height , gender):
    genderType = 21 if gender != "남자" else 22
    weight = pow((height*0.01),2)*genderType   
    return print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다"\
        .format(height,round(weight,2)))

BMI(175,"남자")