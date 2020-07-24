site = "http://naver.com"

my_site = site.replace("http://","")
my_site = my_site.replace(my_site[my_site.find("."):],"")

site_password = str(my_site[:3]) + str(len(my_site)) + str(my_site.count("e")) + "!"

print("{0} 의 비밀번호는 {1} 입니다.".format(site, site_password))
