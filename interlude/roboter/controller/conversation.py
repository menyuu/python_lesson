"""Controller for speaking with robot"""
# modelsモジュールの読み取り
from interlude.roboter.models import robot

def talk_about_restaurant():
    """Function to speak with robot"""
    # robot からオブジェクトの作成
    restaurant_robot = robot.RestaurantRobot()
    restaurant_robot.hello()
    restaurant_robot.recommend_restaurant()
    restaurant_robot.ask_user_favorite()
    restaurant_robot.thank_you()