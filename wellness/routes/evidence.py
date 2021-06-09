from flask import render_template,Blueprint

evidence_page = Blueprint('evidence',__name__,template_folder='templates')
@evidence_page.route('/evidence',methods=['GET','POST'])

def default_activity_page():
    kwargs = {
        'title': 'Evidence',
        'jumbotron': {
            "header": "The science behind Wellness",
            "bg_image": "",
            "text": ""
        },
        'evidencePageContents': [{
            'Title': "Physical",
            "Text": ["Helps Control Weight: For weight management, people vary in how much physical " +
            "exercise they need. A good standard for many people is about 150 minutes of moderate-" + 
            "intensity activity a week. More is needed to lose weight and keep it off.",
            "Reduces the Risk of Cardiovascular Disease: Meeting the 150-minute standard of activity " +
            "reduces the risk of heart disease and stroke, the two leading causes of death in the " +
            "United States. Exercise can also reduce blood pressure and improve cholesterol levels.",
            "Reduces the Risk of Type-2 Diabetes and Metabolic Syndrome: The risk of type 2 diabetes " +
            "and metabolic syndrome is reduced with physical activity.",
            "Reduces the Risk of Some Cancers: Research shows that physically active people have a " +
            "lower risk of colon cancer, and in women, breast cancer. Some research indicates the " +
            "same for endometrial and lung cancer.",
            "Strengthens Bones and Muscles: Exercise can slow the loss of bone density that comes " +
            "with age. It also helps with arthritis.",
            "Improves Mental Health and Mood: Physical activity keeps thinking, learning and judgment " +
            "skills sharp as people age. It also reduces the risk of depression and helps improve " +
            "sleep quality.",
            "Improves Ability to Perform Daily Activities and Prevent Falls: Physical activity helps " +
            "people, especially middle-aged and older adults, do everyday tasks like climbing " +
            "stairs, grocery shopping or playing with children.",
            "Increases Chances of Living Longer: Exercise and physical activity reduces the risk of " +
            "dying at a young age from the leading causes of death. It doesn’t require high amount " +
            "of activity or exercise."
            ]

        },
            {
            "Title": "Emotional",
            "Text": ["Negative attitudes and feelings of helplessness and hopelessness can create " +
            "chronic stress, which upsets the body's hormone balance, depletes the brain chemicals " +
            "required for happiness, and damages the immune system.",
            "Chronic stress can actually decrease our lifespan. Science has now identified that " +
            "stress shortens our telomeres, the \"end caps\" of our DNA strands, which causes us to " +
            "age more quickly.",
            "Poorly managed or repressed anger (hostility) is also related to a slew of health " +
            "conditions, such as hypertension (high blood pressure), cardiovascular disease, " +
            "digestive disorders, and infection.",
            "Benefits of positivity, including faster recovery from cardiovascular stress, better " +
            "sleep, fewer colds, and a greater sense of overall happiness.",
            "Research shows that forgiveness helps us experience better mental, emotional and " +
            "physical health. And it can be learned, as demonstrated by the Stanford Forgiveness " +
            "Project, which trained 260 adults in forgiveness in a 6-week course.",
            "The practice of forgiveness has also been linked to better immune function and a " +
            "longer lifespan. Other studies have shown that forgiveness has more than just a " +
            "metaphorical effect on the heart: it can actually lower our blood pressure and improve " +
            "cardiovascular health as well.",
            "Positive emotions have a scientific purpose—to help the body recover from the ill " +
            "effects of persistent negative emotions. Thus cultivating positivity over time can " +
            "help us become more resilient in the face of crisis or stress."
            ]

        },
            {
            "Title": "Social",
            "Text": ["People who feel more connected to others have lower levels of anxiety and " +
            "depression.",
            "Studies show that social connectedness generates a positive feedback loop of social, " +
            "emotional and physical well-being.",
            "Low levels of social connection are associated with declines in physical and " +
            "psychological health as well as a higher likelihood for antisocial behavior that " +
            "leads to further isolation.",
            "A landmark survey showed that lack of social connectedness predicts vulnerability to " +
            "disease and death beyond traditional risk factors such as smoking, blood pressure, and " +
            "physical activity",
            "Studies show that people with low social connection have higher inflammation at the " +
            "cellular level"
            ]
            


        },
        {
            "Title": "Intellectual",
            "Text": ["Intellectual wellness connotes active engagement in learning, creating, and " +
            "integrating information and experiences.",
            "Support your brain's optimal functioning",
            "Signs of intellectual wellness: curiosity, openness, critical thinking, learning skills",
            "The brain can modify itself and adapt to new information and experiences",
            "Stress is a natural part of life.  We experience stress in varying degrees daily.  " +
            "Getting a handle on stress helps to create balance.",
            "Knowing and practicing a variety of effective time management strategies can help you " +
            "use your time wisely and feel less stressed by having so much to do."
            ]

        }
        ,
            {
            "Title": "Environment",
            "Text": ["Taking small steps to make your environments safer and limiting your exposure " +
            "to potentially harmful substances can help keep you healthier.",
            "Our surroundings and how they influence our choices form the foundation for a healthy " +
            "lifestyle.",
            "It’s estimated that healthcare services account for just 10&#37; of longevity, while " +
            "social and environmental factors account for twice that at 20&#37;, genetics 30&#37;, and " +
            "individual behaviors an estimated 40&#37; (Schroeder, NEJM, 2007).",
            "Being in a high-stress environment such as on a highly-trafficked street will cause the " +
            "brain to signal production of cortisol by the adrenal glands. Elevated cortisol interferes " +
            "with learning and memory, weakens immune function and bone density, and increases weight " +
            "gain, blood pressure and heart disease(Franke, Children, 2014).",
            "Memory and attention spans also benefit from time in nature, with University of Michigan " +
            "psychology researchers pointing to a 20&#37; improvement after spending an hour " +
            "interacting with nature",
            ]

        },
            {
            "Title": "Financial",
            "Text": ""

        },
        {
            "Title": "Spiritual",
            "Text": ""

        },
        {
            "Title": "Occupational",
            "Text": ["Achieving personal satisfaction and fulfillment in one’s work deepens our sense of " +
            "meaning, purpose, worth, and value.",
            "Occupational wellness is connected to other dimensions of wellness and to the " +
            "overall level of wellness someone experiences.",
            "Having a satisfying work life positively impacts physical, mental and emotional wellness.",
            "Engaging in professional development enhances intellectual wellness.",
            "Working collaboratively with coworkers and practicing conflict resolution develops " +
            "social wellness.",
            "Securing work that offers good pay enriches financial wellness."
            ]

        }
        ]
    }
    return render_template('evidence.html', **kwargs)    
