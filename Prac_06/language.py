from Prac_06.programming_language import ProgrammingLanguage
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
c_plus_plus = ProgrammingLanguage("C++", "Static", False, 1983)
java = ProgrammingLanguage("Java", "Static", "True", 1995)
programming_language = ["Ruby,Dynamic,True,1995", "Python,Dynamic,True,1991", "Visual Basic,Static,False,1991",
                        "C++,Static,False,1983", "Java,Static,True,1995"]
ruby.get_field()
ruby.get_typing()
ruby.get_reflection()
ruby.get_field()
for i in range(len(programming_language)):
    language = programming_language[i].split(",")
    language = ProgrammingLanguage(language[0], language[1], language[2], language[3])
    language.get_field()
    language.get_typing()
    language.get_reflection()
    language.get_field()
    print(language.__str__())


# print(str(ruby.is_dynamic()))
#
# print(python.__str__())
# print(visual_basic.__str__())