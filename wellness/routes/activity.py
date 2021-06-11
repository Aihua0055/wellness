from flask import render_template,Blueprint,url_for

activity_page = Blueprint('activity',__name__,template_folder='templates')
@activity_page.route('/activity',methods=['GET','POST'])

def default_activity_page():
    kwargs = {
        'title': 'Activity',
        'jumbotron': {
            "header": "Act NOW",
            "bg_image": "static/images/1182_650_gallery.jpeg",
            "text": ""
        },
        'activityPageContents': [{
            'Title': "Physical Activities",
            "Activities": [
                {"Activities":"Go for a walk outside for 30-45 mins per day or 150 mins of moderate workout per week "},
                {"Sleep":"7-8 hours of sleep a night"},
                {"Nutrition":"1/2 Fresh fruits and veges,1/4 carb,1/4 Protain"},
                {"Breathe":"Deep breathe for 5 mins"},
                {"Standup":"Stand up once an hour for five minutes"},
                ]
        },
            {
            "Title": "Emotional Activities",
            "Activities": [
                {"Hobbies":"Find a hobby that you are passionate about. Go to therapy chat if needed."},
                {"Feelings/Emotions":"Reflect every day,use a journal to record feelings and thoughts "},
                {"Slef - Care":"Take some time to yourself regualarly; Meditation to remain calm and centered;Joined support groups if needed"},
                {"Stress":"Practice deep breathing or other relaxation; Practive finding positives in something that you feel is negative."},
                ]

        },
            {
            "Title": "Social Activities",
            "Activities": [
                {"Community":"Join groups of your interests; Find support groups if necessary"},
                {"New People":"Get out and meet people with your same interests. If you like art, try a gallery;Open to meeting people from diverse backgrounds; Find a place to volunteer"},
                {"Social Time":"Spend quality time regualary with family and friends; Make time to go to places where you can meet new people or visiting a new location; Keep track of when you need to catch up with someone.Organize a calendar of events that would be good ways to connect or reconnect, to friends, like a public concert or a class reunion"},
                ]

        },
            {
            "Title": "Intellectual Activities",
            "Activities": [
                {"Personal Interests":"Reading,music,games, teach a class,try creative arts"},
                {"Education":"Thinkabout continuing education, learn a new language "},
                {"Brain exercise":"Play brain games, mind teasers or fun memory-enhancing games, read up on current affairs locally, nationally, and internationally"},
                {"Conversation":"Take part in discussions, intellectual conversations, debates, or other ways of gaining an enhanced understanding of issues"},
                ]

        },
            {
            "Title": "Environmental Activities",
             "Activities": [
                {"Safe and calm living space":""},
                {"Green life":"Recycle and compost "},
                {"Gardening & Plant":""},
                ]

        }
        ,
            {
            "Title": "Financial Activities",
             "Activities": [
                {"Work":""},
                {"Checking/Savings Accounts":"Have a weekly or monthly budget so you can plan for expenses such as rent and groceries and have a little left over to enjoy "},
                {"Budgeting":""},
                {"Retirement/Other Accounts":"Open a savings account"},
                ]

        },
            {
            "Title": "Spiritual Activities",
             "Activities": [
                {"Meditation":"Meditation or build awareness through journaling"},
                {"Beliefs":"Share beliefs, values and principles with others, as appropriate, as a means of deepening relationships and expanding your world view"},
                {"Involvement":"Find a group that deepens your spirtual practice and helps you connect with others who share your beliefs"},
                {"Time":"Take some time everyday to meditate or reflect on your spiritually; "},
                ]

        },
            {
            "Title": "Occupational Activities",
             "Activities": [
                {"Work Relationships":""},
                {"Balance":" Schedule time for leisure or volunteer work in the community"},
                {"Accomplishment":"In a career that gives you a sense of accomplishment and pride"},
                ]

        }
        ]
    }
    return render_template('activity.html', **kwargs)    
