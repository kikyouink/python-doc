import requests
from pyquery import PyQuery as pq

class Spider:
    markdown=''
    def get_html(self):
        url='https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000'
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'
        }
        doc=pq(requests.get(url,headers=headers).text)
        title=doc('.x-content h4').text()
        info=doc('.x-wiki-info span').text()
        self.markdown+=title+'\n'+info
        main=doc('.x-wiki-content.x-main-content')
        a=main.children('h1,p,pre,ul')
        for i in a.items():
            self.markdown+=self.format(i)
        
        print(self.markdown)
    def format(self,el):
        text=el.text()
        if el.is_('h1'):
            text='# '+text+'\n'
        elif el.is_('p'):
            text+='\n'
        elif el.is_('pre'):
            text='```\n'+text+'```\n'
        elif el.is_('ul'):
            for i in el.children().items():
                text+='- '+i.text()
            
        
        return text
    def save(self,):
        with open('docs/')
s=Spider()
s.get_html()
print('done')