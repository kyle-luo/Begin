def numUniqueEmails(emails):
    actlist = []
    for email in emails:
        split = email.split('@')
        if '+' in split[0]:
            split[0] = split[0][0:split[0].find('+')]
        if '.' in split[0]:
            split[0] = split[0].replace('.','')
        actlist.append(split[0]+split[1])
    actlist = set(actlist)

    return len(actlist)

numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])