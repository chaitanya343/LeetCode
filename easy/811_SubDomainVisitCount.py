def subdomainVisits(cpdomains):
    visitCounts = {}
    for cd in cpdomains:
        cpdom = cd.split(" ")
        count, domain = cpdom[0], cpdom[1]
        subdoms = domain.split('.')
        for i in range(len(subdoms), 0, -1):
            currSd = '.'.join(subdoms[i-1:])
            print(i, currSd, count)
            if currSd in visitCounts:
                visitCounts[currSd] += int(count)
            else:
                visitCounts[currSd] = int(count)
    ans = []
    for sd, count in visitCounts.items():
        ans.append(str(count)+' '+sd)
    return ans

print(subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))