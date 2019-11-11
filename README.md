# mod3_project

This repo contains:
* Description of the project in a PDF
* Three python starter files
* Three test files
* A starter jupyter notebook

We are using OMDB (API) & IMDB (csv) to compare information on movies & TV shows based on their rankings.
These are our hypotheses:
1. Can actor/actress "x" significantly improve the rating of this movie? (Taking the mean rating of films with actor "x" compared to films of the same genre for  the past 5 years without said actor/actress) - One tailed T-Test
2. Do shorter comedy films perform beter? IE films >90minutes will perform worse than those <90minutes. - Two tailed T-Test
3. Is releasing another "genre x" still popular? IE what genre is most popular right now? - Check difference per year for the past 5 years and then predict value for next year? - ANOVA
4. Do films with a budget of >$10,000,000 gross more proportionately than those with <$10,000,000? Looking at the past 5 years (for a certain genre). - One Tailed T-Test