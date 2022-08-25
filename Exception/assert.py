age = 22
assert(age > 18), "Age is less than 18"

#mosglobals.upgrade_status = result
upgrade_fail_msg="mos device upgrade fails"
result = 0
upgrade_status = result
if result:
    print("\n\nUPGRADE SUCCESSFULL!!")
else:
    print("\n\nUPGRADE FAILED!!")
    assert upgrade_status == True, upgrade_fail_msg

