# civi plan

## choose editor + programming language
- VSCode + Python
## choose library
- PyGame
## create a list of features
- Objective: Create a functioning civilization - advance technologically, have 
    many people who are healthy & happy
- Player's role: assign villagers to tasks
- Lose condition: everyone dies (0 health &/or 0 hunger)
- User interface
    - Window with canvas & sprites moving around
    - Mapping tasks to animations (e.g. fishing vs. foraging)
    - Day/night environment
        - How the island looks
    - Island/environment, which has default objects to interact with (bushes, 
        fire pit, etc.)
        - animations (waves, fire moving, etc.)
        - stockpile grows in size as food stores increase
        - farm grows plants (responds to internal stats of farm, how much time 
            user spends doing job)
        - How different food is depicted
    - People
        - people aging (sprite change after age stat)
        - How stats are displayed, increase/decrease in skill level/health 
            changes bars
        - Carrying items/performing tasks sprites
        - Idling sprites
        - Dead sprites
        - Likes/dislikes
    - Stats on structures (internal)
    - How random events are displayed, have choices
    - Alerts when milestones are passed
    - GUI: Buttons to view the map, see progress in advancements, see 
        achievements, go back to menu
- Villager objects
    - Clothes
        - Determined at childhood & does not deteriorate/need to be replenished
    - Idle activities: cannot order villager to do so
        - Random &/or triggered by environment
        - E.g. worrying, playing, giving up, etc.
    - Stats
        - Jobs/tasks
            - Farmer, gatherer, fisher, builder, healer, parent, cook, chief, 
                researcher
                - Requirements/conditions: environmental structure, technology 
                    unlock, achievement unlock (global boolean) or clean lab, 
                    etc.
                    - Altogether determine what task they do/interaction with 
                        environmental structure (e.g. confused, cleaning, 
                        researching)
            - Skill level
                - Impacts speed, success rate of task
                - People can be skilled in multiple jobs
                - Consider decrease in skills
                    - Age
                    - When you haven't practiced a skill for a while
            - Environmental factors stop people from doing a task & switch 
                activities
                - ambient: random (some storms, breaks for celebrations), 
                    day/night)
                    - People do not gather/fish/farm if untrained & will worry 
                        about food if the stockpile is low
                - local (semi-ambient): e.g. event that only affects farmers, 
                    area, some storms
                - individual: death, hunger, health, failure because of skill
                    - the likelihood of this occurring decreases as skill level
                        increases
                - short task that interrupts other task (celebrations)
            - Queuing tasks (automatic)
                - Even low skilled people will gather/fish/farm if food stores 
                    are low
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
                        a higher probability of sickness generally in their 
                        life
                - Carried by mother (sprite)
                - Can be sick/healed
            - Child (2-12)
                - No tasks except eating
                - Various idle activities (e.g. playing, observing, etc.)
                - Can be sick/healed
        - Adult
            - Can do any task
- Environmental objects
    - Job sites (farm, firepit, stone mine, ruins, plots, houses, lab, desk)
        - Sprite changes as technology improves/achievement level increases
    - Random locations (ruins, lagoon, etc.)
        - Need to be cleaned/explored by villager(s) to be usable
        - If unexplored, villager explores, if explored, do some happiness-
            producing task
        - Does not affect skill
    - Cemetery
        - Villager automatically brings/is manually brought to dead villager 
            (bones) to burial site, results in tombstone
        - If not buried, risk of disease for villagers increases
    - Food sources (bushes: berries, ocean: fish/water, mushrooms, coconut 
        trees, farm: livestock, crops)
        - Objects have stats
        - Time regeneration (rate), can be depleted (berry bush, coconut 
            trees, fish/water (high rate))
        - Random (e.g. mushroom clusters (there is some initial amount, 
            after all mushrooms are gathered, pop up around the environment 
            randomly))
        - Work (e.g. farming)
- Jobs/tasks
    - Farming
        - Farmer/villager does a task to farmland (default structure) & obtains 
            crops that are added to the stockpile of food
        - Obtained after progress meter is completed, i.e., some number of 
            tasks is completed by farmers
            - One or more farmers can work on a task to speed up its completion
            - Filled continuously as the farmers do the task
            - Some max number of farmers working on the initial plot of land
        - With advancements in technology, can increase the size/capacity of 
            the farmland
            - Requires a builder to modify the farm
    - Cooking
        - Firepit, requires wood & people to make the fire (task)
            - Unlimited once unlocked
        - Task involves taking some amount of raw food from the stockpile, 
            going to the fire, cooking food, returning cooked food to the 
            stockpile
        - Individual task
        - Some max number of cooks at the firepit
    - Gathering
        - Individual task
        - Task involves going to a mushroom cluster or the berry bush, getting 
            food, bringing it to the stockpile
    - Fishing
        - Individual task
        - Task involves going to the ocean, fishing, bringing fish to the 
            stockpile
    - Healing (plants)
        - Time regeneration
        - Healer needs to study the plant before it can be used for healing
        - Task involves studying sick person, gathering plant, using plant to 
            heal
            - Less skilled healers choose incorrect plant & do not heal sick
            - One healer to one sick villager
        - Some illnesses can go away on their own, if that occurs while the 
            healer is doing the task, healer stops task
    - Building
        - Virtually unlimited rocks, time regeneration for wood
        - Builder needs to explore the quarry & wood source before it can be 
            used for building
        - Task involves collecting stone (quarry), wood (trees, driftwood), 
            building on plot (default structure), replanting trees
            - Plot can be housing, farm, lab, etc. throughout the island
            - One or more builders can work on a task to speed up its 
                completion
            - Filled continuously as the builders do the task
            - Some max number of builders working on the initial plot of land 
    - Breeding
        - Once house is built, people can breed
        - Need one male villager & one female villager to do the task
        - Automatically fail task if its an invalid pairing (child, same sex, 
            etc.)
        - Task involves going to a house, no longer visible, & leave with a 
            newborn
        - Eventually population will exceed food replenishment
    - Religious teaching
        - Task involves going to the ampitheatre, sharing a message
    - Researching
        - Research bench next to every job site
            - Increases progress bar for next level of technology
            - Research barrier until research lab is unlocked
        - Lab unlocked after cleaned
- Resources
    - Population (metric)
        - Increases after successful breeding
        - Decreases after death of villager
    - Food (can be spent, affects happiness)
        - Jobs produce raw or ready-to-eat food
            - Raw: Fish/seafood, livestock, crops
            - Ready-to-eat: Berries, mushrooms, cooked
    - Technology (advancements in farming, construction, medicine, fertility, 
        spiritual)
        - Unlock more technologies once progress bar is completed for each 
            category
- Random events
    - Occur at any time point in the game
    - Occur while performing a job/task
    - Can impact resources, abilities, etc.
    - E.g. Should the villager eat the strange fish? Discovers a food source or 
        gets sick
## decide MVP
- UI
    - Top-down view of island (one canvas)
        - Terrain
        - Villagers
        - Job sites
    - Display resource stats
        - Population
        - Food
        - Technology
    - Click on villager to view villager stats
        - Popup window display that takes up the whole screen
        - Age
        - Hunger
        - Health
        - Skills (only one active, gathering)
    - Mouse controls for player to change villager's position
        - Two choices
            - Move villager to some structure, it interacts with it
            - Move villager to no structure, override villager's initial task & 
                assign it to idle
- Backend
    - Things the backend can receive from the frontend
        - Orders for villagers to go to a position
    - Preset villager stats
    - Things that happen as time progresses (natural processes)
        - Age increases
        - Hunger decreases
        - Villager moves
        - Death if age is at some number and/or hunger is at 0
    - One food source: berry bush (unlimited)
        - Villagers interact with berry bush
        - Food resource stat increases
        - Skill of villager performing task increases upon task completion
        - Villager proceeds with task until interrupted
    - One idle task: look at berry bush
        - Automatic task