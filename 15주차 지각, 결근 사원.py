company={'김','이','박','최','황'}
late={'이','박', '황'}
absent={'김','이','황'}
late_absent=late.union(absent)
bonus=company-late_absent
overtime=late&absent
print('보너스 대상자 : ', bonus)
print('야근 대상자 : ', overtime)