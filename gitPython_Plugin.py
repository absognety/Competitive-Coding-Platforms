from bs4 import BeautifulSoup
import urllib
import git
import os


path = 'C:/Users/cvikas10'
dirs = os.listdir(path)
os.makedirs(os.path.join(path,'CrowdStrike_Project'))
os.chdir(os.path.join(path,'CrowdStrike_Project'))

pageURL = 'http://hck.re/crowdstrike'
web_page = urllib.request.Request(pageURL)
response = urllib.request.urlopen(web_page)
soup = BeautifulSoup(response.read(),'html.parser')
branch_info = list(soup.findAll('td'))

cleaned_info1 = [soup.find("td").text]
cleaned_info1.append(soup.find('td').find_next_sibling('td').text)
cleaned_info1.append(soup.find('td').find_next_sibling('td').find_next_sibling('td').text)

cleaned_info2 = ['Cs2']
cleaned_info2.append('https://bitbucket.org/zeeshan_07/cs2/src/master/')
cleaned_info2.append('crowdstrike2')


git.Repo.clone_from(cleaned_info1[1],os.path.join(path,'CrowdStrike_Project'))
repo = git.Repo(os.path.join(path,'CrowdStrike_Project'))
print (repo.branches)
print (repo.heads)
feature_branch = repo.create_head('feature')
current = repo.branches['feature'] #current = repo.active_branch
master = repo.branches['master']
base = repo.merge_base(current,master)

repo.index.merge_tree(master,base=base)

repo.index.commit('Merge master into feature',
                  parent_commits=(current.commit, master.commit))

#remote = repo.create_remote('upstream','http://hck.re/tHEZGP')
repo.git.push('origin','feature')



#Repeat the same process for Cs2