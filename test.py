from llm_mail import get_subject_and_body

res = get_subject_and_body('write a mail to john doe about online scams')

print(res[0])
print(res[1])