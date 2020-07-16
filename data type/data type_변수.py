# 애완동물을 소개해 주세요~

animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

# print("우리집" + animal + "의 이름은" + name + "이에요")
# hobby = "공놀이"
# print(name, "는 ", age, "살이며,", hobby, "을 아주 좋아해요.")
# print(name + "는 어른일까요? " + str(is_adult))

print("우리집 {0}의 이름은 {1}에요.".format(animal, name))
print("{0}는 {1}살이며, {2}를 아주 좋아해요.".format(name, age, hobby))
print("{0}는 어른일까요? {1}".format(name, is_adult))