# Microsoft-Hackathon-AI-Learning

**A 3rd place Hackathon winner Adaptify! An app for translating learning material into a more comprehensible way for neurodiverse learning based on behavioural science. A revolutionary educational platform that creates personalized learning experiences for neurodivergent learners through AI-driven customization.
**

## **Overview**
This repository contains the project developed during the Microsoft Hackathon, focusing on utilizing Artificial Intelligence to create personalized learning experiences for neurodiverse students. Our solution aims to address the challenges faced by neurodivergent learners in traditional educational systems by providing tailored study materials and an inclusive, interactive learning platform.

## **Presentation:** https://www.canva.com/design/DAGYVxDRHAA/rilhUI0RLE0nc8Pk0a_Www/edit?utm_content=DAGYVxDRHAA&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

## **Problem Statement**
Neurodiverse students often face difficulties in traditional learning environments due to a "one-size-fits-all" approach. These challenges include:
- Lack of personalized learning experiences.
- Inadequate accessibility tools.
- Limited support for diverse learning preferences and needs.

Our goal is to create a solution that bridges these gaps by leveraging AI to provide customized and accessible educational tools.

## **Solution**
We developed a platform that uses a questionnaire-based approach to assess individual learning preferences and needs. Based on the responses, the platform generates a personalized, interactive study space designed to help users achieve their academic goals. Key features of our solution include:
- **Personalized Learning Plans**: Tailored strategies based on user preferences and neurodiversity profiles.
- **Accessibility Tools**: Features like visual aids, hands-on activities, and movement-based learning methods.
- **Interactive Environment**: An engaging platform that adapts to the user's unique learning style.

## **How It Works**
1. **Questionnaire**: Users complete a 20-question survey designed to identify their learning preferences and challenges.
2. **AI Processing**: The responses are processed using a Large Language Model (LLM) chain to generate personalized recommendations.
3. **Learning Strategies**: The platform provides tailored strategies such as written materials, visual aids, hands-on practice, or movement-based activities.
4. **Interactive Platform**: Users interact with a dynamic study space that supports their specific needs.

### Example Outputs:
- For a user with Auditory Processing Disorder (APD): Emphasis on written materials and visual aids while minimizing verbal explanations.
- For a Kinesthetic Learner: Hands-on experiments, trial-and-error approaches, and movement-based activities.

## **Features**
- **Neurodiversity Survey**: A comprehensive questionnaire to assess individual needs.
- **AI-Powered Insights**: LLM chains analyze survey responses to create tailored learning strategies.
- **Customizable Study Space**: A user-friendly interface that adapts to different learning styles.


## Example Learning Profiles
https://docs.google.com/forms/d/1S5jHng6XQWV18n-niDjZL18oCJY2IhqhpEN2lUmacY0/edit#response=ACYDBNjVWy1URJrF8C0QZHtMv2BLLc1SH-TIMjjFm3Uu6Ie6akJczzAc663DNLqtIBZfAlg
As above questionaire responses 1 and two are fed into the LLM to produce different analysis of the users learning preferences...

**Profile Type 1: APD Focus**
- Minimized verbal explanations
- Enhanced written materials
- Visual aid integration
- Hands-on practice components


**Profile Type 2: Kinesthetic Learner**
- Hands-on experience focus
- Trial and error approach
- Intuitive learning methods
- Virtual tours and simulations
- Movement-based learning integration

## Next Step: LLM Chain
- The first LLM chain will use the questionaire with an answering key to score the users learning preferences

'''python
          
          content = '''You are a helpful assistant used to convert questionaire answers into a short summary on how to best explain learning content to the use 
          Here is a guide to understand the results Scoring Guide
          Diagnosis Question 1 answers:
          Dyslexia: struggles with written instructions (may prefer diagrams)
          Dysgraphia: struggles with writing and organising thoughts (may benefit from bullet points)
          Dyscalculia: Trouble with Numbers, (maths may need to be explained in other ways)
          APD: Difficult with verbal explanation(avoid text to speech)
          VPD: Trouble with visual understanding (avoid diagrams etc.)
          ADHD: Prefers simple explanations, engaging content
          None: Ignore this question
          
          Count your answers:
          Mostly A's: Visual Learner
          Mostly B's: Auditory Learner
          Mostly C's: Read/Write Learner
          Mostly D's: Kinesthetic Learner
          Visual Learners prefer diagrams, charts, and visual representations.
          Auditory Learners learn best through listening and discussion.
          Read/Write Learners prefer written information and note-taking.
          Kinesthetic Learners learn best through hands-on experience and practice.
          
          Please output a summary of the best way to explain learning content to the user based on their answers to the questionnaire provide in the prompt.'''
          
          
          prompt1 = "Auditory Processing Disorder (APD), ADHD	c) Read a detailed written analysis	b) Talk to people who've been there	a) Watch video tutorials	d) Figure it out by experimenting	a) Follow the diagram illustrations	c) Reading about techniques	c) Reading materials and notes	c) Write detailed instructions	a) Create diagrams or mind maps	c) Remember written words"
          
          prompt2 = "None,	d) Review practical examples from my work	d) Explore virtual tours or simulations	d) Try it hands-on through trial and error	d) Figure it out by experimenting	d) Try putting pieces together intuitively	b) Listening to explanations	d) Hands-on experiments	d) Walk with the person		d) Remember actions and movements"
          
          
          
          # Function to get response from Azure OpenAI
          def get_response(prompt):
              try:
                  messages = [
                      {"role": "system", "content": content},
                      {"role": "user", "content": prompt}
        ]
        
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

'''


- The analysis from first LLM chain is fed into the second LLM chain to provide it with context on the users learning preferences

'''python

    def get_response(prompt):
        try:
            messages = [
                {"role": "system", "content": "Please present the learning material in a way the user can understand using the following summary of them: " + summary},
                {"role": "user", "content": prompt}
            ]
        
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=0.7,
        )
        print(summary)
        return response.choices[0].message.content + "\n" + "Here is the relevant summary from the previous LLM Chain: " + summary
    except Exception as e:
        return f"Error: {str(e)}"
  '''
- This will output a learning material that has been altered to the users needs


## Check examples file for real inputs/outputs



## Contributing

We welcome contributions to improve the platform's effectiveness for neurodiverse learners. Please submit pull requests or open issues for suggestions and improvements.



