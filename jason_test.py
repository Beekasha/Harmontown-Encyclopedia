# import json

# data = {}
# data['people'] = []
# data['people'].append({
#     'name': 'Scott',
#     'website': 'stackabuse.com',
#     'from': 'Nebraska'
# })
# data['people'].append({
#     'name': 'Larry',
#     'website': 'google.com',
#     'from': 'Michigan'
# })
# data['people'].append({
#     'name': 'Tim',
#     'website': 'apple.com',
#     'from': 'Alabama'
# })

# with open('data.txt', 'w') as outfile:
#     json.dump(data, outfile)

import json

data = {}
data['episodes'] = []
data['episodes'].append({
    'id': 'Scott',
    'location': 'stackabuse.com',
    'transcription': 'Nebraska',
    'confidence': 'confidence'
})
data['episodes'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['episodes'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)


# harmontown = {
#     "episodes": [
#         {
#             "ep-id": {
#                 "location": 
#                 "text":
#             }
#         }
#     ]

    
# }

# {
#     "Harmontown": {

#         "title": "$OEPISODE-TITLE-TEXT",
#         "ep-id": {

#         }
#     }
# }


{
    "title": "Harmontown",
    "episodes": [
        {
            "episode-id": "$$$2010292",
            "location-in-seq": "$$$CU",
            "transcription": "$$$transcription"
            "confidence": "$$$confidence"
        }
        # {episode object}
        # {episode object}
        # {episode object}
    ]
}