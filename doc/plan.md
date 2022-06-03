# civi plan

## choose editor + programming language
- VSCode + Python
## choose library
- PyGame
## create a list of features
- Objective: Create a functioning civilization - advance technologically, have many people who are healthy & happy
- Player's role: assign villagers to tasks
- Lose condition: everyone dies (0 health &/or 0 hunger)
- User interface
    - Window with canvas & sprites moving around
    - Mapping tasks to animations (e.g. fishing vs. foraging)
    - Day/night environment
        - How the island looks
    - Island/environment, which has default objects to interact with (bushes, fire pit, etc.)
        - animations (waves, fire moving, etc.)
        - stockpile grows in size as food stores increase
        - farm grows plants (responds to internal stats of farm, how much time user spends doing job)
        - How different food is depicted
    - People
        - people aging (sprite change after age stat)
        - How stats are displayed, increase/decrease in skill level/health changes bars
        - Carrying items/performing tasks sprites
        - Idling sprites
        - Dead sprites
        - Likes/dislikes
    - Stats on structures (internal)
    - How random events are displayed, have choices
    - Alerts when milestones are passed
    - GUI: Buttons to view the map, see progress in advancements, see achievements, go back to menu
- Villager objects
    - Clothes
        - Determined at childhood & does not deteriorate/need to be replenished
    - Idle activities: cannot order villager to do so
        - Random &/or triggered by environment
        - E.g. worrying, playing, giving up, etc.
    - Stats
        - Jobs/tasks
            - Farmer, gatherer, fisher, builder, healer, parent, cook, chief, researcher
                - Requirements/conditions: environmental structure, technology 
                    unlock, achievement unlock (global boolean) or clean lab, 
                    etc.
                    - Altogether determine what task they do/interaction with 
                        environmental structure (e.g. confused, cleaning, 
                        researching)
            - Skill level
                - Impacts speed/output of task
                - People can be skilled in multiple jobs
                - Consider decrease in skills
                    - Age
                    - When you haven't practiced a skill for a while
            - Environmental factors stop people from doing a task & switch 
                activities
                - ambient: random (some storms, breaks for celebrations), 
                    day/night)
                    - People do not gather/fish/farm if untrained & will worry about food 
                        if the stockpile is low
                - local (semi-ambient): e.g. event that only affects farmers, 
                    area, some storms
                - individual: death, hunger, health, failure because of skill
                    - the likelihood of this occurring decreases as skill level
                        increases
                - short task that interrupts other task (celebrations)
            - Queuing tasks (automatic)
                - Even low skilled people will gather/fish/farm if food stores are low
                - Maybe based on the needs of the community
            - Small celebration after finishing a task (part of task 
                completion)
        - Hunger
            - Amount of food necessary to satisfy hunger is determined by age
            - Villagers passively go to ready-to-eat food storage to eat
            - Villagers will leave their job to eat if hungry
                - Can be overridden by player, but this may kill villagers
            - Hunger drains over time (drain rate)
            - Max hunger capacity
            - People fight about food if the stockpile is low (health/happiness 
                decreases)
        - Health
            - Sickness (people are unable to work &/or eat)
                - Reduces health steadily
                - Random (eating bad food, etc.)
                - Result of hunger being low
                - Can spread & catch disease
                    - Particularly for healers
                - Can impact the rate at which hunger decreases
            - Injury
                - Can deal damage or make villager incapacitated
                - Random
                - Job/tasks (cutting self on bush or hitting with hammer)
        - Happiness
            - Increase
                - Celebrations (achievement unlocked)
                - Leisure activities (swimming in lagoon, exploration)
                - Spirituality (attending chief's gatherings)
                - Childbirth
            - Decrease
                - Hunger, low food stockpile (worrying)
                - Poor health
                - Failing tasks
                - Doing a job they don't like
                - Childbirth
                - Spirituality (attending chief's gatherings)
                    - Some people enjoy/do not enjoy
            - 0 happiness makes people not eat/work
        - Likes/dislikes
            - Random
    - Age
        - Ability to do jobs/tasks change (child to adult)
        - Death
            - Random chance of death increases at a certain age
                - Old age
                - Sickness
        - Fertility
            - Able to conceive at some age
            - Probability of conceiving decreases as age increases (different 
                rates for men & women)
            - Pregnancy
                - Cannot conceive
                - Requires more food to satisfy hunger
                - Can't work after a certain point in pregnancy
        - Childhood
            - Newborn (0-1)
                - No tasks (nursed by mother for food)
                    - Mother is sick: hunger is replenished more slowly
                    - Death of mother: babies can be fed regular food, but has 
                        a higher probability of sickness generally in their life
                - Carried by mother (sprite)
                - Can be sick/healed
            - Child (2-12)
                - No tasks except eating
                - Various idle activities (e.g. playing, observing, etc.)
                - Can be sick/healed
        - Adult
            - Can do any task
- Environmental objects
    - Food sources (bushes: berries, ocean: fish/water, mushrooms, coconut 
        trees, farm: livestock, crops)
        - Objects have stats
        - Time regeneration (rate), can be depleted (berry bush, coconut 
            trees, fish/water (high rate))
        - Random (e.g. mushroom clusters (there is some initial amount, 
            after all mushrooms are gathered, pop up around the environment 
            randomly))
        - Work (e.g. farming)
    - Farming
    
    - Healing (plants)
        - Time regeneration
    - Job sites (farm, stone mine, ruins, plots, houses, lab, desk)
        - Sprite changes as technology improves/achievement level increases
    - Random locations (ruins, lagoon, etc.)
    - Cemetery
- Resources
    - Population (metric)
    - Food (can be spent, affects happiness)
        - Jobs produce raw or ready-to-eat food
            - Raw: Fish/seafood, livestock, crops
            - Ready-to-eat: Berries, mushrooms, cooked
    - Technology (spend to unlock more technologies)
- Random events
    - Occur at any time point in the game
    - Occur while performing a job/task
    - Can impact resources, abilities, etc.