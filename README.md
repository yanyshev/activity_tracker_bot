# Activity Tracker Bot

## Available Commands
- /start \
Activate the bot
- /help \
List all available commands
- /set_profile \
Start setting up the profile
- /check_progress \
Check your progress
- /log_water \
Log water consumption, the format is `/log_water <amount consumed in ml>` \
API [OpenWeather](https://openweathermap.org/) is used to determine the water goal based on a temperature info. The rule is following:
$Water Standard = 10 * Weight + max(t(C) // 25, 0)$
- /log_food \
Log food consumption, the format is `/log_food <food product>`. API [OpenFoodFacts](https://world.openfoodfacts.org/) is used to initialize food's nutritional info. After it, input the weight, g
- /log_workout
Log workout activity, the format is `/log_workout <workout type> <activity in minutes>`. No API is used

## Structure of the Project
- bot.py \
Main file of the project. Initializes the bot, manages it startup, etc.
- config.py \
Contains configuration setting and environment variables. For proper work requires `.env` file with API keys
- utils \
  (directory) Contains logging functions, error handling API functions, etc.
- handlers \
(directory) Contains handlers distinguished by functionality and bot logic
