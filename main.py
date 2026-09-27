from model.user import User
from service.user_service import UserService
user_service = UserService()

from service.activity_service import ActivityService
activity_service = ActivityService()

from model.practice import Practice
from service.practice_service import PracticeService
practice_service = PracticeService()

from model.performance import Performance
from service.performance_service import PerformanceService
performance_service = PerformanceService()

from model.timebox import Timebox
from service.timebox_service import TimeboxService
timebox_service = TimeboxService()

from service.reading_service import ReadingService
reading_service = ReadingService()

while True:

    print("\n===== english learning timebox =====")
    print("1. add user")
    print("2. view activities")
    print("3. record practice")
    print("4. record performance")
    print("5. add timebox")
    print("6. view reading content")
    print("7. exit")

    choice = input("enter your choice: ")

    if choice == "1":
        name = input("enter name: ")
        email = input("enter email: ")

        user = User(name=name,email=email)

        user_service.add_user(user)

    elif choice == "2":
        activities = activity_service.get_all_activities()

        print("\n----- activities -----")

        for activity in activities:
            print(activity[0], activity[1], "-", activity[2], "minutes")
        

    elif choice == "3":
        user_id = int(input("enter user id: "))
        activity_id = int(input("enter activity id: "))
        practice_date = input("enter date (yyyy-mm-dd): ")
        planned_minutes = int(input("enter planned minutes: "))
        actual_minutes = int(input("enter actual minutes: "))
        status = input("enter status (completed/pending): ")

        practice = Practice(
            user_id=user_id,
            activity_id=activity_id,
            practice_date=practice_date,
            planned_minutes=planned_minutes,
            actual_minutes=actual_minutes,
            status=status
        )

        practice_service.add_practice(practice)
    elif choice == "4":
        user_id = int(input("enter user id: "))
        activity_id = int(input("enter activity id: "))
        score = float(input("enter score (0-100): "))
        mistake_count = int(input("enter mistake count: "))
        performance_date = input("enter date (yyyy-mm-dd): ")

        performance = Performance(
            user_id=user_id,
            activity_id=activity_id,
            score=score,
            mistake_count=mistake_count,
            performance_date=performance_date
        )

        performance_service.add_performance(performance)

    elif choice == "5":
        user_id = int(input("enter user id: "))
        activity_id = int(input("enter activity id: "))
        recommended_minutes = int(input("enter recommended minutes: "))
        timebox_date = input("enter date (yyyy-mm-dd): ")

        timebox = Timebox(
            user_id=user_id,
            activity_id=activity_id,
            recommended_minutes=recommended_minutes,
            timebox_date=timebox_date
        )

        timebox_service.add_timebox(timebox)
    elif choice == "6":
        content = reading_service.get_all_content()

        print("\n----- reading content -----")

        for story in content:
            print("\nID:", story[0])
            print("Title:", story[1])
            print("Difficulty:", story[3])
            print("Estimated time:", story[4], "minutes")
            print("Story:", story[2])

    elif choice == "7":
        print("thank you")
        break

    else:
        print("invalid choice")