import speech_recognition
import pyttsx3
from datetime import date, datetime
import webbrowser

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_mouth.setProperty('voice', 'english_rp+f3')
robot_mouth.setProperty('rate', 160)

robot_brain = "Welcome to the Neo Culture Technology Club booth at club day. You can ask me one of the " \
              "following: \n" \
              "1. Upcoming events\n" \
              "2. Our Department\n" \
              "3. Club day's activities"
print("Robot: " + robot_brain)

robot_mouth.say(robot_brain)
robot_mouth.runAndWait()

while True:
    url = None
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        audio = robot_ear.listen(mic)
        print("Robot...")
        try:
            you = robot_ear.recognize_google(audio)
        except:
            you = ""

    if "bye" in you:
        robot_brain = "Goodbye my friend, have a nice day!"
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    if you == "":
        robot_brain = "Can you ask me again?"
    elif "event" in you or "events" in you or "induction" in you or "day" in you:
        robot_brain = "We will have the Induction Day on 15 July at Room 1.2.26. You can register the event here"
        url = "https://rmiteduau.sharepoint.com/:i:/s/NCT-NeoCultureTechClubCoreTeam/EahE0QczjH5Cu_-kwwHKsy4BXY7pm1QJRi8mZJe_3gUobg?e=RfAK8m"
    elif "department" in you or "position" in you:
        robot_brain = "We are recruiting for 4 positions:\n1.Project Management, \n2.Human Resources, \n3.Marketing\n" \
                      "4. Graphic Designer\n5.Financial Assistant. Which position you want to discover more? "
    elif "project" in you or "management" in you:
        robot_brain = "Here is the job description of Project Management, You can view it here"
        url = "https://bit.ly/JD_for_project_management"
    elif "human" in you or "hr" in you or "resources" in you:
        robot_brain = "Here is the job description of Human Resources, You can view it here"
        url = "https://bit.ly/JD_for_human_resource "
    elif "marketing" in you or "media" in you:
        robot_brain = "Here is the job description of Marketing and Media, You can view it here"
        url = "https://bit.ly/JD_for_marketing"
    elif "finance" in you or "financial" in you or "assistant" in you:
        robot_brain = "Here is the job description of Financial Assistant, You can view it here"
        url = "https://bit.ly/JD_for_finance_assistant"
    elif "graphic" in you or "designer" in you:
        robot_brain = "Here is the job description of Financial Assistant, You can view it here"
        url = "https://rmiteduau.sharepoint.com/sites/NCT-NeoCultureTechClubCoreTeam/Shared%20Documents/Forms" \
              "/AllItems.aspx?id=%2Fsites%2FNCT%2DNeoCultureTechClubCoreTeam%2FShared%20Documents%2FHuman%20Resource" \
              "%20Department%20%28HR%29%2FRecruitment%2FJobs%20Description%2FMedia%20Department%2Epdf&parent=%2Fsites" \
              "%2FNCT%2DNeoCultureTechClubCoreTeam%2FShared%20Documents%2FHuman%20Resource%20Department%20%28HR%29" \
              "%2FRecruitment%2FJobs%20Description&p=true&ga=1"
    elif "apply" in you:
        robot_brain = "Here is the QR code for joining the Neo Culture Technology Club"
        url = "https://rmiteduau-my.sharepoint.com/personal/s3927469_rmit_edu_vn/_layouts/15/onedrive.aspx?listurl=https%3A%2F%2Frmiteduau%2Esharepoint%2Ecom%2Fsites%2FNCT%2DNeoCultureTechClubCoreTeam%2FShared%20Documents&viewid=447310c1%2D4a32%2D4e4e%2D88d0%2Dd208c7de4896&login_hint=S3927469%40rmit%2Eedu%2Evn&id=%2Fsites%2FNCT%2DNeoCultureTechClubCoreTeam%2FShared%20Documents%2FEvent%20Department%2F2022%2FSem%20B%2FRecruitment%2FQRCode%20for%20Neo%20Culture%20Tech%20Club%20Recruitment%20Sem%20B%5F2022%20%281%29%2Epng&parent=%2Fsites%2FNCT%2DNeoCultureTechClubCoreTeam%2FShared%20Documents%2FEvent%20Department%2F2022%2FSem%20B%2FRecruitment"
    elif "activities" in you or "activity" in you:
        robot_brain = "We have the tarot card and the lucky draw. You can ask the booth stander for enjoying with us"
    else:
        robot_brain = "Can you ask me again?"

    print("Robot: " + robot_brain)

    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
    robot_brain = ""
    print("Change")

    if url is None:
        continue
    webbrowser.register('chrome',
                        None,
                        webbrowser.BackgroundBrowser(
                            "/snap/bin/firefox"))
    webbrowser.get('chrome').open(url)
