import webapp2
from google.appengine.ext import ndb
import jinja2
import os

import content


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))


# VisitorInput class to define a comment object for a database of comments:
class VisitorInput(ndb.Model):
    nickname = ndb.StringProperty()
    comment = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)


# --------------------------Handler Classes--------------------------------------

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)
    
    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class MainPage(Handler):
    def get(self):
        stages = content.STAGES
        url_main = self.request.url.replace('?error=error', '')
        
        error = self.request.get('error','')
        error_statement = ''
        if error:
            error_statement = 'No nickname or no comment was entered. Try again!'
        query = VisitorInput.query().order(-VisitorInput.date)
        nickname = ''
        comment = ''
        date = ''
        for visit in query:
            nickname = visit.nickname
            comment = visit.comment
            date = visit.date
        self.render("main_page.html", stages=stages, url_main=url_main, 
                    query=query, nickname=nickname, comment=comment, 
                    date=date, error_statement=error_statement)


    def post(self):
        nickname = self.request.get('nickname').strip()
        comment = self.request.get('comment').strip()

       # Allow ability to create comment objects and save to Datastore
        if nickname and comment:
            visit = VisitorInput(nickname=nickname, comment=comment)
            visit.put()
            
            # Datastore to update
            import time
            time.sleep(.1)
            self.redirect('/')
        else:
            self.redirect('/?error=error')
        
class Stage(Handler):
    def get(self):
        p = self.request.get('p', 0)
        url_stage = self.request.url
        url_main = self.request.url.replace('stage?p='+ p, '')
        stage = content.STAGES[int(p)][3]
        lesson_path = 'lesson?p=' + p + '&q='
        stage_num = int(p) + 1
        self.render("stage.html", p=p, stage=stage, 
                    url_main=url_main, url_stage=url_stage,
                    lesson_path=lesson_path, stage_num=stage_num)


class Lesson(Handler):
    def get(self):
        p = self.request.get('p', 0)
        q = self.request.get('q', 0)
        url_lesson = self.request.url
        url_stage = self.request.url.replace('lesson?p='+ p + '&q=' + q, 'stage?p=' + p)
        url_main = url_stage.replace('stage?p='+ p, '')
        lesson = content.STAGES[int(p)][3][int(q)]
        stage_num = int(p) + 1
        lesson_num = int(q) + 1
        self.render("lesson.html", q=q, p=p, lesson=lesson, 
                    url_stage=url_stage, url_main=url_main,
                    url_lesson=url_lesson, stage_num=stage_num, 
                    lesson_num=lesson_num)


app = webapp2.WSGIApplication([("/", MainPage), ("/stage", Stage), ("/lesson", Lesson)], 
                              debug=True)

