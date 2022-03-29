from statsbombpy import sb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from FCPython import createPitch

competition_df = pd.DataFrame(sb.competitions())

#Competition id of the 2018 World Cup = 43, season id = 3

world_cup_matches = pd.DataFrame(sb.matches(competition_id=43,season_id=3))
# Argentina vs Crotia match id 7545

arg_cro = pd.DataFrame(sb.events(7545))

shots = arg_cro[arg_cro.type == 'Shot'].set_index('id')


pitch_width = 120
pitch_height = 80
fig,ax = createPitch(pitch_width,pitch_height,'yards','gray')

#a = plt.Circle((1,2),5)
#ax.add_patch(a)
#fig

home_team = 'Argentina'
away_team = 'Croatia'
for i,shot in shots.iterrows():
    x = shot['location'][0]
    y = shot['location'][1]

    goal = shot['shot_outcome']=='Goal'
    team_name = shot['team']

    circle_size = 2
    circle_size = np.sqrt(shot['shot_statsbomb_xg']*15)

    if team_name == home_team:
        if goal:
            shot_circle = plt.Circle((x,pitch_height-y),circle_size,color = 'red')
            plt.text((x+1),pitch_height-y+1,shot['player'])
        else:
            shot_circle = plt.Circle((x,pitch_height-y),circle_size,color = 'red')
            shot_circle.set_alpha(.2)
    
    if team_name == away_team:
        if goal:
            shot_circle = plt.Circle((pitch_width-x,y),circle_size,color = 'blue')
            plt.text((pitch_width-x+1),y+1,shot['player'])

        else:
            shot_circle = plt.Circle((pitch_width-x,y),circle_size,color = 'blue')
            shot_circle.set_alpha(.2)
        
    ax.add_patch(shot_circle)

plt.text(5,75,away_team + ' shots')
plt.text(80,75,home_team + ' shots')

plt.title('Argentina vs Croatia')

fig.set_size_inches(10, 7)
fig.savefig('ARG_CRO_2018_WC_SHOTMAP.png', dpi=300) 

plt.show()
