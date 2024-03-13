import json
import os

# Market Segmentation Matrix data
market_segmentation_matrix = [
    {"#": 1, "Market Segment Name": "End User", "Description": "This is the person who is actually using the product not the economic buyer or the champion (more on this in step 12) – it is not a company or a general organization but real people"},
    {"#": 2, "Market Segment Name": "Task", "Description": "What exactly is it that the end user does that you will significantly affect or allow her to do that she could not do before?"},
    {"#": 3, "Market Segment Name": "Benefit", "Description": "What is the benefit that you believe the end user will get?"},
    {"#": 4, "Market Segment Name": "Urgency of Need", "Description": "What is the level of urgency to solve the problem or capture the new opportunity for the end user?"},
    {"#": 5, "Market Segment Name": "Example End Users", "Description": "Who are example users that you can, have or will talk to so as to validate your perceptions on this market segment?"},
    {"#": 6, "Market Segment Name": "Lead Customers", "Description": "Who are the influential customers (i.e., lighthouse customers) that if they buy, others will take note & likely follow?"},
    {"#": 7, "Market Segment Name": "Willingness to Change", "Description": "How conservative is this market segment? How open are they to change? Is there something to force change (i.e., impending crisis)?"},
    {"#": 8, "Market Segment Name": "Frequency of Buying", "Description": "How often do they buy new products? What does their buying cycle look like at a high level?"},
    {"#": 9, "Market Segment Name": "Concentration of Buyers", "Description": "How many different buyers are there in this market segment? Is it a monopoly? Oligopoly (a small number of buyers)? Or many competitive buyers?"},
    {"#": 10, "Market Segment Name": "Other relevant market considerations", "Description": "This allows for customization for your segment for relevant considerations such as “high employee turnover”, “very low margins/ commodity”, “high growth industry”, “high virality effect (i.e., WOM -Word of Mouth”, etc."},
    {"#": 11, "Market Segment Name": "Size of Market (# of end users)", "Description": "Estimation of the number of end users to a relevant range (10’s, 100’s, 1K’s, 10K’s, 100K’s, 1M, etc.)"},
    {"#": 12, "Market Segment Name": "Est. value of end user", "Description": "A first pass estimate of the value of each end user, again to a relevant order of magnitude so we can make some relative decisions now but then we will dive much deeper into this and other numbers later"},
    {"#": 13, "Market Segment Name": "Competition/ alternatives", "Description": "What will be your competition from the end users’ perspective? Of course, there is the “do nothing option” but who else would be competitors if they analyzed their options?"},
    {"#": 14, "Market Segment Name": "Other components needed for a full solution", "Description": "Since most customers will only buy a full solution and not components, what are the other elements needed to construct a full solution to achieve the benefits above? These are the complementary assets that you do not currently have but would need to build or acquire to give the end user a total solution."},
    {"#": 15, "Market Segment Name": "Important partners", "Description": "Who are the partners or distributors you will have to work with to fit into the workflow (e.g., data must come out vendor A’s system and then be picked up at the end by vendor B’s system) or business processes (e.g., the end user gets all his product via distribution channel C)"},
    {"#": 16, "Market Segment Name": "Other relevant personal considerations", "Description": "In many market segmentation analyses, there are additional important factors that should be considered. This could be things like where the market segment is geographically centered, values match to the founding team, existing knowledge and contacts in the market, etc."}
]

# Determine the path for the "tools" subdirectory relative to this script
script_dir = os.path.dirname(os.path.abspath(__file__))
tools_dir = os.path.join(script_dir, 'tools')

# Ensure the "tools" subdirectory exists
if not os.path.exists(tools_dir):
    os.makedirs(tools_dir)

# Define the file path for the JSON file within the "tools" subdirectory
json_file_path = os.path.join(tools_dir, 'market_segmentation_matrix.json')

# Write the market segmentation matrix to the JSON file
with open(json_file_path, 'w', encoding='utf-8') as f:
    json.dump(market_segmentation_matrix, f, ensure_ascii=False, indent=4)

print(f'Market Segmentation Matrix saved to {json_file_path}')
