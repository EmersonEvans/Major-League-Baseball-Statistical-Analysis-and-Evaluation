import statistics
import math

print("Major League Baseball Statistical Analysis and Evaluation - Emerson Evans")
print()
while True:
    print("(1) Explanation of Statistics")
    print("(2) Player Analysis - User Input")
    print("(3) Team Analysis - User Input")
    print("(4) 2023 Player Statistics")
    print("(5) Team Statistics - 2021 to 2023")
    print("(6) 2025 Projection")
    print("(7) Exit Program")
    print()
    tab = input("Enter the number of the tab you would like to explore: ")
    if tab == "1":
        #explanation
        print()
        print("In this project, I created 3 new statistics to analyze MLB batters: Produced Runs Average (PRA), Earned Bases Average (EBA), and Bases Plus Runs (BPR). In addition, I designed a formula which can be used to compare the strength of MLB teams: Adjusted Bases Plus Runs (aBPR). Using these statistics, I examined league wide batter numbers in the 2023 season (tab 4), looked at team averages from 2021 - 2024 (tab 5), and created a formula which I used to project standings for the 2025 season (tab 6). Below are my equations for each statistic as well as a brief explanation of their worth.")
        print()
        print() 
        print("PRA:")
        print()
        print("(R + RBI - HR) / PA")
        print("Tells us the average number of runs a hitter produces for their team each plate appearance. At the end of the day, the goal of an offense is to score runs, meaning the most important way to value a hitter is by their ability to produce runs at an efficient rate. In the 2023 season, the average PRA was 0.206.")
        print()
        print()
        print("EBA:")
        print()
        print("(TB + BB + HBP + SB + IBB - CS - DP) / PA")
        print("Calculates the average number of bases a hitter earns for their team each plate appearance. Without runners on base, offenses are stagnant, relying solely on the long ball. Getting on base and swiping bags are crucial for a great offense, which is why EBA is a critical way to examine player worth. In 2023, the average EBA was 0.464.")
        print()
        print()
        print("BPR:")
        print()
        print("PRA + EBA")
        print("Combines the number of runs a player produces with their ability to get on base. In 2023, the average BPR was 0.654.")
        print()
        print()
        print("aBPR:")
        print()
        print("(PA / 162) * (BPR) - ((9 * WHIP) + ERA))")
        print("Is a team statistic which shows the number of bases and runs produced by the offense per game subtracted by the average number of bases and runs given up by the pitching staff. Numbers are slightly skewed upwards since some runs and bases are counted twice. For example, if one player hits a homerun to drive in someone else, both of their PRAs go up, meaning the run is double counted. The average team aBPR from 2021 to 2023 was 8.857.")
        print()   
        
    elif tab == "2":
        #user input player
        #According to statistics gathered in the 2023 season, player_name would be in the __ percentile for pra, __ for eba, and _for bpr
        #print that at end
        print()

        print("In this tab, you are able to calculate the PRA, EBA, and BPR of any player of your choice, past or present. Follow the instructions given by inputting the correct numbers into the applicable prompt.")
        print()

        again = "y"
        while again == "y":
            first_name = input("Enter player first name: ")
            last_name = input("Enter player last name: ")
            team_name = input("Enter team abbreviation: ")
            season = input("""Enter the season you are wishing to calculate statistics for. If you are looking at a player's entire career write "career": """)
    
            pa = int(input("Enter Plate Appearances: "))
            runs = int(input("Enter Runs Scored: "))
            homeruns = int(input("Enter Homeruns: "))
            rbis = int(input("Enter Runs Batted In: "))
            stolen_bases = int(input("Enter Stolen Bases: "))
            caught_stealing = int(input("Enter Caught Stealing: "))
            walks = int(input("Enter Walks: "))
            total_bases = int(input("Enter Total Bases: "))
            double_plays = int(input("Enter Double Plays: "))
            HBP = int(input("Enter Hit By Pitches: "))
            intent_walks = int(input("Enter Intentional Walks: "))  

            pra = (runs + rbis - homeruns) / pa
            eba = (total_bases + walks + HBP + stolen_bases + intent_walks - caught_stealing - double_plays) / pa
            bpr = pra + eba

            format_pra = format(pra, ".3f")
            format_eba = format(eba, ".3f")
            format_bpr = format(bpr, ".3f")
            print()

            if season.lower() == "career":
                print(first_name, last_name, "-- Career")
            else:
                print(first_name, " ", last_name, " (", team_name, ") -- ", season, sep="")

            print()
            print("PRA: ", format_pra)
            print("EBA: ", format_eba)
            print("BPR: ", format_bpr)

            print()
            again = input("Would you like to look at another player? (Y)es or (n)o? ")
            again = again.lower()
            print()

            if again == "y":
                continue
            else:
                print("Returning to home page.")
                print()
                break
            
    elif tab == "3":
        #user input team
        #add in leaguewide percentile... use numbers from number 4 !!!!!! 
        print()
        print("In this tab, you are able to calculate the aBPR of any team of your choice")
        print()
        
        again = "y"
        while again == "y":
            your_city = input("Enter the city the team plays in: ")
            your_team = input("Enter the team name: ")
            your_season = input("Enter the season you would like to look at: ")

            if your_season == "2024":
                games = int(input("Enter the number of games the team has played: "))
            else:
                games = 162

            pa = int(input("Enter Team Plate Appearances: "))
            runs = int(input("Enter Team Runs Scored: "))
            homeruns = int(input("Enter Team Homeruns: "))
            rbis = int(input("Enter Team Runs Batted In: "))
            stolen_bases = int(input("Enter Team Stolen Bases: "))
            caught_stealing = int(input("Enter Team Caught Stealing: "))
            walks = int(input("Enter Team Walks: "))
            total_bases = int(input("Enter Team Total Bases: "))
            double_plays = int(input("Enter Team Double Plays: "))
            HBP = int(input("Enter Team Hit By Pitches: "))
            intent_walks = int(input("Enter Team Intentional Walks: "))  

            pra = (runs + rbis - homeruns) / pa
            eba = (total_bases + walks + HBP + stolen_bases + intent_walks - caught_stealing - double_plays) / pa
            bpr = pra + eba

            whip = float(input("Enter Team Walks and Hits per Inning Pitched: "))
            era = float(input("Enter Team Earned Run Average: "))

            mult = (pa / games) * bpr
            against =  (9 * whip) + era
            abpr = mult - against
            good_abpr = format(abpr, ".3f")

            print()
            print("In ", your_season, " the ", your_city, " ", your_team, " had an aBPR of, ", abpr, sep="")
            print()
            again = input("Would you like to look at another team? (Y)es or (n)o? ")
            again = again.lower()

            if again == "y":
                print()
                continue
            else:
                print()
                print("Returning to home page.")
                print()
                break

    elif tab == "4":
        #2023
        #make sure to add another percentile (whole MLB) use function from tab 2
        
        print()
        print("This tab serves as a search engine for players' statistics during the 2023 season. The database includes all hitter who accumulated more than 200 plate appearances that season. Enter a player name (first and last) and the program will show their 2023 numbers.")
        print()
        print("After the player's numbers, in the parentheses, is the percentile amongst their position that these statistics land them in.") 
        print()
        print("Be sure to type in the player's full name with correct capitalizations and spacing")
        print()
        again = "y"
        while again == "y": 
            
            name_2023 = input("Enter player name: ")
            position_2023 = input("Enter the player's position (c, 1b, 2b, 3b, ss, lf, cf, rf, dh): ")

            def z_to_percentile(z):
                cdf = 0.5 * (1 + math.erf(z / math.sqrt(2)))
                percentile = cdf * 100
                return percentile
                
            if position_2023 == "c":
                p_2023 = ["Adley Rutschman", "William Contreras", "Salvador Perez", "Cal Raleigh", "Keibert Ruiz", "Will Smith", "J.T. Realmuto", "Elias Diaz", "Tyler Stephenson", "Jonah Heim", "Willson Contreras", "Shea Langeliers", "Sean Murphy", "Francisco Alvarez", "Alejandro Kirk", "Yan Gomes", "Martin Maldonado", "Yasmani Grandal", "Connor Wong", "Gabriel Moreno", "Yander Diaz", "Jake Rogers", "Christian Vazquez", "Patrick Bailey", "Blake Sabol", "Ryan Jeffers", "Christian Bethancourt", "Nick Fortes", "Matt Thaiss", "Danny Jansen", "Eric Haase", "Travis dArnaud", "Jacob Stallings", "Gary Sanchez", "Kyle Higashioka", "Andrew Knizner", "Freddy Fermin", "Bo Naylor", "Victor Caratini", "James McCann", "Austin Hedges", "Reese McGuire", "Endy Rodriguez", "Austin Barnes", "Luke Maile", "Logan OHoppe", "Seby Zavala", "Carlos Perez", "Jason Delay", "Luis Campusano"]
                teams_2023 = ["BAL", "MIL", "KC", "SEA", "WSH", "LAD", "PHI", "COL", "CIN", "TEX", "STL", "OAK", "ATL", "NYM", "TOR", "CHC", "HOU", "CWS", "BOS", "AZ", "HOU", "DET", "MIN", "SF", "SF", "MIN", "TB", "MIA", "LAA", "TOR", "CLE", "ATL", "MIA", "SD", "NYY", "STL", "KC", "CLE", "MIL", "BAL", "TEX", "BOS", "PIT", "LAD", "CIN", "LAA", "AZ", "OAK", "PIT", "SD"]
                pra_2023 = [.21, .241, .2, .216, .185, .247, .209, .202, .197, .275, .206, .190, .256, .210, .164, .232, .133, .143, .203, .2, .233, .205, .169, .198, .195, .224, .214, .164, .176, .246, .15, .202, .141, .228, .185, .212, .209, .235, .181, .199, .137, .146, .181, .12, .181, .191, .145, .164, .198, .287]
                eba_2023 = [.496, .489, .438, .499, .425, .486, .498, .426, .41, .469, .515, .443, .516, .461, .382, .427, .366, .378, .429, .416, .517, .471, .375, .380, .436, .534, .386, .316, .423, .525, .297, .425, .326, .524, .419, .432, .438, .557, .403, .394, .231, .379, .368, .28, .412, .513, .342, .386, .374, .471]
                bpr_2023 = []
                for i in range(len(pra_2023)):
                    bpr_2023 += [pra_2023[i] + eba_2023[i]]
                pra_avg = 0.196
                eba_avg = 0.425
                bpr_avg = 0.622

                pra_sd = statistics.stdev(pra_2023)
                eba_sd = statistics.stdev(eba_2023)
                bpr_sd = statistics.stdev(bpr_2023)

                if name_2023 in p_2023:
                    index = p_2023.index(name_2023)
                    p_team = teams_2023[index]
                    p_pra = pra_2023[index]
                    p_eba = eba_2023[index]
                    p_bpr = bpr_2023[index]
                    p_bpr = float(format(p_bpr, ".3f"))

                    z_score_pra = (p_pra - pra_avg) / pra_sd
                    z_score_eba = (p_eba - eba_avg) / eba_sd
                    z_score_bpr = (p_bpr - bpr_avg) / bpr_sd
    

                    perc_pra = z_to_percentile(z_score_pra)
                    perc_eba = z_to_percentile(z_score_eba)
                    perc_bpr = z_to_percentile(z_score_bpr)

                    g_perc_pra = format(perc_pra, ".2f")
                    g_perc_eba = format(perc_eba, ".2f")
                    g_perc_bpr = format(perc_bpr, ".2f")

                    print()
                    print(name_2023, "--", p_team, "-- Catcher")
                    print("PRA: ", p_pra, " (", g_perc_pra, "%)", sep="")
                    print("EBA: ", p_eba, " (", g_perc_eba, "%)", sep="")
                    print("BPR: ", p_bpr, " (", g_perc_bpr, "%)", sep="")

                    print()
                    again = input("Would you like to look up another player? (Y)es or (n)o? ")
                    again = again.lower()

                    if again == "y":
                        print()
                        continue
                    else:
                        print()
                        print("Returning to home page.")
                        print()
                else:
                    print("Player not found, try again")
                    print()
                    continue
            elif position_2023 == "1b":
                p_2023 = ["Freddie Freeman", "Nathaniel Lowe", "Matt Olson", "Paul Goldschmidt", "Spencer Torkelson", "Vladimir Guerrero", "Ty France", "Spencer Steer", "Christian Walker", "Pete Alonso", "Carlos Santana", "Josh Bell", "Andrew Vaughn", "Yandy Diaz", "Jose Abreu", "Dominic Smith", "Jeimer Candelario", "Jake Cronenworth", "LaMonte Wade", "Triston Casas", "Josh Naylor", "Ryan Noda", "Ryan Mountcastle", "Garrett Cooper", "Wilmer Flores", "Donovan Solano", "Anthony Rizzo", "Luke Raley", "Ryan OHearn", "Rowdy Tellez", "Nick Pratto", "Joey Gallo", "Yuli Gurriel", "Alex Kirilloff", "Elehuris Montero", "C.J. Cron", "Trey Mancini", "Vinnie Pasquantino", "Joey Votto", "Christian Strand"]
                teams_2023 = ["LAD", "TEX", "ATL", "STL", "DET", "TOR", "SEA", "CIN", "AZ", "NYM", "MIL", "MIA", "CWS", "TB", "HOU", "WSH", "CHC", "SD", "SF", "BOS", "CLE", "OAK", "BAL", "SD", "SF", "MIN", "NYY", "TB", "BAL", "MIL", "KC", "MIN", "MIA", "MIN", "COL", "LAA", "CHC", "KC", "CIN", "CIN"]
                pra_2023 = [.279, .213, .294, .210, .221, .214, .188, .206, .236, .249, .228, .169, .205, .252, .226, .155, .217, .176, .177, .213, .267, .204, .243, .188, .194, .169, .176, .212, .255, .171, .177, .175, .167, .204, .221, .227, .209, .158, .207, .220]
                eba_2023 = [.642, .465, .654, .521, .485, .479, .403, .529, .545, .553, .478, .457, .447, .550, .404, .408, .523, .439, .505, .550, .529, .507, .470, .427, .529, .449, .418, .567, .511, .407, .406, .518, .389, .502, .443, .421, .373, .473, .504, .506]
                bpr_2023 = []
                for i in range(len(pra_2023)):
                    bpr_2023 += [pra_2023[i] + eba_2023[i]]
                pra_avg = 0.209
                eba_avg = 0.484
                bpr_avg = 0.688

                pra_sd = statistics.stdev(pra_2023)
                eba_sd = statistics.stdev(eba_2023)
                bpr_sd = statistics.stdev(bpr_2023)

                if name_2023 in p_2023:
                    index = p_2023.index(name_2023)
                    p_team = teams_2023[index]
                    p_pra = pra_2023[index]
                    p_eba = eba_2023[index]
                    p_bpr = bpr_2023[index]
                    p_bpr = float(format(p_bpr, ".3f"))

                    z_score_pra = (p_pra - pra_avg) / pra_sd
                    z_score_eba = (p_eba - eba_avg) / eba_sd
                    z_score_bpr = (p_bpr - bpr_avg) / bpr_sd
    

                    perc_pra = z_to_percentile(z_score_pra)
                    perc_eba = z_to_percentile(z_score_eba)
                    perc_bpr = z_to_percentile(z_score_bpr)

                    g_perc_pra = format(perc_pra, ".2f")
                    g_perc_eba = format(perc_eba, ".2f")
                    g_perc_bpr = format(perc_bpr, ".2f")

                    print()
                    print(name_2023, "--", p_team, "-- First Base")
                    print("PRA: ", p_pra, " (", g_perc_pra, "%)", sep="")
                    print("EBA: ", p_eba, " (", g_perc_eba, "%)", sep="")
                    print("BPR: ", p_bpr, " (", g_perc_bpr, "%)", sep="")

                    print()
                    again = input("Would you like to look up another player? (Y)es or (n)o? ")
                    again = again.lower()

                    if again == "y":
                        print()
                        continue
                    else:
                        print()
                        print("Returning to home page.")
                        print()
                else:
                    print("Player not found, try again.")
                    print()
                    continue

            elif position_2023 == "2b":
                p_2023 = ["Marcus Semien", "Nico Hoerner", "Gleyber Torres", "Ozzie Albies", "Ketel Marte", "Jeff McNeil", "Bryson Stott", "Ha-Seong Kim", "Luis Arraez", "Andres Gimenez", "Whit Merrifield", "Amed Rosario", "Thairo Estrada", "Jonathan India", "Tommy Edman", "Brandon Drury", "Entrique Hernandez", "Mauricio Dubon", "Luis Garcia", "Nolan Gorman", "Michael Massey", "Adam Frazier", "Brice Turang", "Luis Rengifo", "Brandon Lowe", "Jose Altuve", "Edouard Julien", "Elvis Andrus", "Andy Ibanez", "Ji Hwan Bae", "Brendan Donovan", "Kyle Farmer", "Josh Rojas", "Jorge Polanco", "Cavan Biggio", "Owen Miller", "Miguel Vargas", "Zack Gelof", "Jose Caballero", "Harold Castro", "Nicky Lopez", "Santiago Espinal", "Zack Short", "Jordan Westburg", "Alan Trejo", "Christian Arroyo"]
                teams_2023 = ["TEX", "CHC", "NYY", "ATL", "AZ", "NYM", "PHI", "SD", "MIA", "CLE", "TOR", "LAD", "SF", "CIN", "STL", "LAA", "LAD", "HOU", "WSH", "STL", "KC", "BAL", "MIL", "LAA", "TB", "HOU", "MIN", "CWS", "DET", "PIT", "STL", "MIN", "SEA", "MIN", "TOR", "MIL", "LAD", "OAK", "SEA", "COL", "ATL", "TOR", "DET", "BAL", "COL", "BOS"]
                pra_2023 = [.256, .228, .198, .261, .232, .185, .195, .203, .211, .2, .206, .224, .185, .231, .195, .226, .211, .228, .212, .233, .178, .233, .165, .202, .241, .268, .199, .190, .188, .226, .191, .228, .237, .210, .251, .162, .201, .193, .211, .200, .214, .209, .170, .202, .203, .214]
                eba_2023 = [.537, .471, .488, .553, .529, .437, .484, .503, .488, .472, .424, .409, .464, .476, .470, .493, .374, .425, .405, .541, .416, .444, .388, .497, .509, .585, .529, .397, .452, .396, .491, .431, .409, .516, .464, .424, .451, .577, .507, .319, .389, .374, .415, .443, .392, .340]
                bpr_2023 = []
                for i in range(len(pra_2023)):
                    bpr_2023 += [pra_2023[i] + eba_2023[i]]
                pra_avg = 0.210
                eba_avg = 0.456
                bpr_avg = 0.667

                pra_sd = statistics.stdev(pra_2023)
                eba_sd = statistics.stdev(eba_2023)
                bpr_sd = statistics.stdev(bpr_2023)

                if name_2023 in p_2023:
                    index = p_2023.index(name_2023)
                    p_team = teams_2023[index]
                    p_pra = pra_2023[index]
                    p_eba = eba_2023[index]
                    p_bpr = bpr_2023[index]
                    p_bpr = float(format(p_bpr, ".3f"))

                    z_score_pra = (p_pra - pra_avg) / pra_sd
                    z_score_eba = (p_eba - eba_avg) / eba_sd
                    z_score_bpr = (p_bpr - bpr_avg) / bpr_sd
    

                    perc_pra = z_to_percentile(z_score_pra)
                    perc_eba = z_to_percentile(z_score_eba)
                    perc_bpr = z_to_percentile(z_score_bpr)

                    g_perc_pra = format(perc_pra, ".2f")
                    g_perc_eba = format(perc_eba, ".2f")
                    g_perc_bpr = format(perc_bpr, ".2f")

                    print()
                    print(name_2023, "--", p_team, "-- Second Base")
                    print("PRA: ", p_pra, " (", g_perc_pra, "%)", sep="")
                    print("EBA: ", p_eba, " (", g_perc_eba, "%)", sep="")
                    print("BPR: ", p_bpr, " (", g_perc_bpr, "%)", sep="")

                    print()
                    again = input("Would you like to look up another player? (Y)es or (n)o? ")
                    again = again.lower()

                    if again == "y":
                        print()
                        continue
                    else:
                        print()
                        print("Returning to home page.")
                        print()
                
                else:
                    print("Player not found, try again.")
                    print()
                    continue
            elif position_2023 == "ss":
                p_2023 = ["Bobby Witt", "Trea Turner", "Francisco Lindor", "Xander Bogaerts", "Willy Adames", "J.P. Crawford", "Dansby Swanson", "Jeremy Pena", "Ezequiel Tovar", "CJ Abrams", "Bo Bichette", "Anthony Volpe", "Carlos Correa", "Javier Baez", "Corey Seager", "Orlando Arcia", "Tim Anderson", "Geraldo Perdomo", "Wander Franco", "Ezequiel Duran", "Elly De La Cruz", "Jon Berti", "Miguel Rojas", "Matt McLain", "Paul DeJong", "Jorge Mateo", "Gabriel Arias", "Nick Allen", "Zach Neto", "Brandon Crawford", "Joey Wendle", "Casey Schmitt", "Garrett Hampson", "Josh Smith", "Tucupita Marcano", "Liover Peguero", "Nick Ahmed"]
                teams_2023 = ["KC", "PHI", "NYM", "SD", "MIL", "SEA", "CHC", "HOU", "COL", "WSH", "TOR", "NYY", "MIN", "DET", "TEX", "ATL", "CWS", "AZ", "TB", "TEX", "CIN", "MIA", "LAD", "CIN", "SF", "BAL", "CLE", "OAK", "LAA", "SF", "MIA", "SF", "MIA", "TEX", "PIT", "PIT", "AZ"]
                pra_2023 = [.235, .22, .255, .183, .202, .219, .218, .194, .223, .210, .203, .168, .184, .197, .282, .214, .145, .226, .216, .189, .230, .186, .177, .246, .163, .243, .151, .137, .191, .194, .160, .191, .198, .164, .141, .188, .138]
                eba_2023 = [.555, .527, .555, .483, .459, .516, .478, .42, .426, .513, .479, .454, .416, .364, .655, .439, .326, .459, .53, .474, .515, .448, .35, .563, .370, .429, .377, .307, .438, .375, .327, .339, .444, .414, .391, .394, .362]
                bpr_2023 = []
                for i in range(len(pra_2023)):
                    bpr_2023 += [pra_2023[i] + eba_2023[i]]
                pra_avg = 0.197
                eba_avg = 0.442
                bpr_avg = 0.639

                pra_sd = statistics.stdev(pra_2023)
                eba_sd = statistics.stdev(eba_2023)
                bpr_sd = statistics.stdev(bpr_2023)

                if name_2023 in p_2023:
                    index = p_2023.index(name_2023)
                    p_team = teams_2023[index]
                    p_pra = pra_2023[index]
                    p_eba = eba_2023[index]
                    p_bpr = bpr_2023[index]
                    p_bpr = float(format(p_bpr, ".3f"))

                    z_score_pra = (p_pra - pra_avg) / pra_sd
                    z_score_eba = (p_eba - eba_avg) / eba_sd
                    z_score_bpr = (p_bpr - bpr_avg) / bpr_sd
    

                    perc_pra = z_to_percentile(z_score_pra)
                    perc_eba = z_to_percentile(z_score_eba)
                    perc_bpr = z_to_percentile(z_score_bpr)

                    g_perc_pra = format(perc_pra, ".2f")
                    g_perc_eba = format(perc_eba, ".2f")
                    g_perc_bpr = format(perc_bpr, ".2f")

                    print()
                    print(name_2023, "--", p_team, "-- Shortstop")
                    print("PRA: ", p_pra, " (", g_perc_pra, "%)", sep="")
                    print("EBA: ", p_eba, " (", g_perc_eba, "%)", sep="")
                    print("BPR: ", p_bpr, " (", g_perc_bpr, "%)", sep="")

                    print()
                    again = input("Would you like to look up another player? (Y)es or (n)o? ")
                    again = again.lower()

                    if again == "y":
                        print()
                        continue
                    else:
                        print()
                        print("Returning to home page.")
                        print()
                
                else:
                    print("Player not found, try again.")
                    print()
                    continue

            elif position_2023 == "3b":
                p_2023 = ["Alex Bregman", "Austin Riley", "Eugenio Suarez", "Jose Ramirez", "Rafael Devers", "Ryan McMahon", "Gunnar Henderson", "Nolan Arenado", "Alec Bohm", "Manny Machado", "Matt Chapman", "Max Muncy", "Isaac Paredes", "DJ LeMahieu", "J.D. Davis", "Jake Burger", "KeBryan Hayes", "Zach McKinstry", "Maikel Garcia", "Josh Jung", "Jace Peterson", "Ramon Urias", "Brett Baty", "Mike Moustakas", "Brian Anderson", "Yoan Moncada", "Taylor Walls", "Aledmys Diaz", "Nick Senzel", "Jean Segura", "Andruw Monasterio", "Eduardo Escobar", "Patrick Wisdom", "Edmundo Sosa", "Nick Madrigal", "Jordan Diaz", "Nick Maton", "Ildemaro Vargas", "Emmanual Rivera", "Rodolfo Castro", "Kevin Newman", "Royce Lewis", "Evan Longoria", "Gio Urshela", "Matt Duffy", "Jared Triolo"]
                teams_2023 = ["HOU", "ATL", "SEA", "CLE", "BOS", "COL", "BAL", "STL", "PHI", "SD", "TOR", "LAD", "TB", "NYY", "SF", "MIA", "PIT", "DET", "KC", "TEX", "AZ", "BAL", "NYM", "LAA", "MIL", "CWS", "TB", "OAK", "CIN", "MIA", "MIL", "LAA", "CHC", "PHI", "CHC", "OAK", "DET", "WSH", "AZ", "PHI", "CIN", "MIN", "AZ", "LAA", "KC", "PIT"]
                pra_2023 = [.243, .248, .205, .207, .239, .203, .248, .225, .247, .226, .177, .282, .242, .149, .205, .217, .211, .166, .204, .237, .153, .210, .170, .205, .191, .190, .223, .131, .236, .132, .197, .184, .219, .180, .204, .126, .181, .206, .201, .152, .209, .305, .177, .193, .148, .23]
                eba_2023 = [.49, .537, .447, .579, .552, .464, .532, .466, .445, .474, .491, .544, .539, .436, .441, .546, .469, .423, .414, .483, .405, .409, .357, .409, .402, .445, .476, .346, .430, .307, .397, .359, .543, .427, .405, .369, .386, .367, .375, .371, .407, .59, .439, .364, .359, .498]
                bpr_2023 = []
                for i in range(len(pra_2023)):
                    bpr_2023 += [pra_2023[i] + eba_2023[i]]
                pra_avg = 0.202
                eba_avg = 0.443
                bpr_avg = 0.646

                pra_sd = statistics.stdev(pra_2023)
                eba_sd = statistics.stdev(eba_2023)
                bpr_sd = statistics.stdev(bpr_2023)

                if name_2023 in p_2023:
                    index = p_2023.index(name_2023)
                    p_team = teams_2023[index]
                    p_pra = pra_2023[index]
                    p_eba = eba_2023[index]
                    p_bpr = bpr_2023[index]
                    p_bpr = float(format(p_bpr, ".3f"))

                    z_score_pra = (p_pra - pra_avg) / pra_sd
                    z_score_eba = (p_eba - eba_avg) / eba_sd
                    z_score_bpr = (p_bpr - bpr_avg) / bpr_sd
    

                    perc_pra = z_to_percentile(z_score_pra)
                    perc_eba = z_to_percentile(z_score_eba)
                    perc_bpr = z_to_percentile(z_score_bpr)

                    g_perc_pra = format(perc_pra, ".2f")
                    g_perc_eba = format(perc_eba, ".2f")
                    g_perc_bpr = format(perc_bpr, ".2f")

                    print()
                    print(name_2023, "--", p_team, "-- Third Base")
                    print("PRA: ", p_pra, " (", g_perc_pra, "%)", sep="")
                    print("EBA: ", p_eba, " (", g_perc_eba, "%)", sep="")
                    print("BPR: ", p_bpr, " (", g_perc_bpr, "%)", sep="")

                    print()
                    again = input("Would you like to look up another player? (Y)es or (n)o? ")
                    again = again.lower()

                    if again == "y":
                        print()
                        continue
                    else:
                        print()
                        print("Returning to home page.")
                        print()
                
                else:
                    print("Player not found, try again.")
                    print()
                    continue
            elif position_2023 == "lf":
                p_2023 = ["Kyle Schwarber", "Steven Kwan", "Juan Soto", "Ian Happ", "Randy Arozarena", "Corbin Carroll", "Bryan Reynolds", "Christian Yelich", "Bryan De La Cruz", "Andrew Benintendi", "Lourdes Gurriel", "Daulton Varsho", "Masataka Yoshida", "Austin Hays", "Jurickson Profar", "Eddie Rosario", "Tommy Pham", "Randal Grichuk", "Chas McCormick", "Nolan Jones", "David Peralta", "Robbie Grossman", "Tony Kemp", "Jarred Kelenic", "Willi Castro", "Taylor Ward", "Edward Olivares", "Chris Taylor", "Akil Baddoo", "Alec Burleson", "Oswaldo Cabrera", "Corey Julks", "JJ Bleday", "Stone Garrett", "Tyler ONeill", "Stuart Fairchild", "Matt Wallner", "Rob Refsnyder", "Mitch Haniger", "Trevor Larnach", "Kevin Pillar", "Jake Cave"]
                teams_2023 = ["PHI", "CLE", "SD", "CHC", "TB", "AZ", "PIT", "MIL", "MIA", "CWS", "AZ", "TOR", "BOS", "BAL", "SD", "ATL", "AZ", "LAA", "HOU", "COL", "LAD", "TEX", "OAK", "SEA", "MIN", "LAA", "KC", "LAD", "DET", "STL", "NYY", "HOU", "OAK", "WSH", "STL", "CIN", "MIN", "BOS", "SF", "MIN", "ATL", "PHI"]
                pra_2023 = [.229, .198, .242, .216, .237, .259, .227, .258, .19, .18, .208, .182, .221, .224, .177, .227, .222, .197, .234, .241, .225, .226, .153, .197, .208, .227, .184, .24, .176, .179, .179, .192, .172, .262, .147, .224, .272, .239, .214, .274, .252, .167]
                eba_2023 = [.567, .446, .606, .515, .512, .619, .506, .544, .422, .417, .473, .444, .462, .47, .413, .459, .516, .478, .565, .644, .398, .455, .384, .49, .531, .465, .491, .521, .468, .398, .361, .415, .449, .487, .466, .475, .591, .407, .384, .481, .432, .394]
                bpr_2023 = []
                for i in range(len(pra_2023)):
                    bpr_2023 += [pra_2023[i] + eba_2023[i]]
                pra_avg = 0.213
                eba_avg = 0.475
                bpr_avg = 0.689

                pra_sd = statistics.stdev(pra_2023)
                eba_sd = statistics.stdev(eba_2023)
                bpr_sd = statistics.stdev(bpr_2023)

                if name_2023 in p_2023:
                    index = p_2023.index(name_2023)
                    p_team = teams_2023[index]
                    p_pra = pra_2023[index]
                    p_eba = eba_2023[index]
                    p_bpr = bpr_2023[index]
                    p_bpr = float(format(p_bpr, ".3f"))

                    z_score_pra = (p_pra - pra_avg) / pra_sd
                    z_score_eba = (p_eba - eba_avg) / eba_sd
                    z_score_bpr = (p_bpr - bpr_avg) / bpr_sd
    

                    perc_pra = z_to_percentile(z_score_pra)
                    perc_eba = z_to_percentile(z_score_eba)
                    perc_bpr = z_to_percentile(z_score_bpr)

                    g_perc_pra = format(perc_pra, ".2f")
                    g_perc_eba = format(perc_eba, ".2f")
                    g_perc_bpr = format(perc_bpr, ".2f")

                    print()
                    print(name_2023, "--", p_team, "-- Left Field")
                    print("PRA: ", p_pra, " (", g_perc_pra, "%)", sep="")
                    print("EBA: ", p_eba, " (", g_perc_eba, "%)", sep="")
                    print("BPR: ", p_bpr, " (", g_perc_bpr, "%)", sep="")

                    print()
                    again = input("Would you like to look up another player? (Y)es or (n)o? ")
                    again = again.lower()

                    if again == "y":
                        print()
                        continue
                    else:
                        print()
                        print("Returning to home page.")
                        print()
                
                else:
                    print("Player not found, try again.")
                    print()
                    continue

            elif position_2023 == "cf":
                p_2023 = ["Julio Rodriguez", "Brandon Nimmo", "Luis Robert", "James Outman", "Cody Bellinger", "TJ Friedl", "Trent Grisham", "Leody Taveras", "Michael Harris", "Jack Suwinski", "Myles Straw", "Lars Nootbaar", "Esteury Ruiz", "Brandon Marsh", "Cedric Mullins", "Alex Call", "Brenton Doyle", "Riley Greene", "Joey Wiemer", "Kevin Kiermaier", "Alek Thomas", "Mike Tauchman", "Michael Taylor", "Jazz Chisholm", "Jose Siri", "Jarren Duran", "Mike Trout", "Isiah Kiner-Falefa", "Adam Duvall", "Harrison Bader", "Jake Meyers", "Drew Waters", "Manuel Margot", "Mickey Moniak", "Kyle Isbel", "Aaron Hicks", "Dylan Carlson", "Luis Matos"]
                teams_2023 = ["SEA", "NYM", "CWS", "LAD", "CHC", "CIN", "SD", "TEX", "ATL", "PIT", "CLE", "STL", "OAK", "PHI", "BAL", "WSH", "COL", "DET", "MIL", "TOR", "AZ", "CHC", "MIN", "MIA", "TB", "BOS", "LAA", "NYY", "BOS", "CIN", "HOU", "KC", "TB", "LAA", "KC", "BAL", "STL", "SF"]
                pra_2023 = [.242, .195, .222, .235, .299, .218, .187, .217, .213, .208, .154, .211, .179, .225, .242, .166, .2, .185, .188, .211, .201, .259, .201, .214, .245, .215, .221, .194, .232, .224, .191, .190, .217, .204, .236, .231, .192, .142]
                eba_2023 = [.552, .521, .587, .531, .57, .552, .450, .466, .519, .552, .357, .509, .481, .538, .49, .396, .397, .493, .432, .471, .415, .476, .492, .533, .53, .572, .561, .385, .575, .41, .44, .454, .414, .514, .415, .478, .412, .399]
                bpr_2023 = []
                for i in range(len(pra_2023)):
                    bpr_2023 += [pra_2023[i] + eba_2023[i]]
                pra_avg = 0.210
                eba_avg = 0.482
                bpr_avg = 0.693

                pra_sd = statistics.stdev(pra_2023)
                eba_sd = statistics.stdev(eba_2023)
                bpr_sd = statistics.stdev(bpr_2023)

                if name_2023 in p_2023:
                    index = p_2023.index(name_2023)
                    p_team = teams_2023[index]
                    p_pra = pra_2023[index]
                    p_eba = eba_2023[index]
                    p_bpr = bpr_2023[index]
                    p_bpr = float(format(p_bpr, ".3f"))

                    z_score_pra = (p_pra - pra_avg) / pra_sd
                    z_score_eba = (p_eba - eba_avg) / eba_sd
                    z_score_bpr = (p_bpr - bpr_avg) / bpr_sd
    

                    perc_pra = z_to_percentile(z_score_pra)
                    perc_eba = z_to_percentile(z_score_eba)
                    perc_bpr = z_to_percentile(z_score_bpr)

                    g_perc_pra = format(perc_pra, ".2f")
                    g_perc_eba = format(perc_eba, ".2f")
                    g_perc_bpr = format(perc_bpr, ".2f")

                    print()
                    print(name_2023, "--", p_team, "-- Center Field")
                    print("PRA: ", p_pra, " (", g_perc_pra, "%)", sep="")
                    print("EBA: ", p_eba, " (", g_perc_eba, "%)", sep="")
                    print("BPR: ", p_bpr, " (", g_perc_bpr, "%)", sep="")

                    print()
                    again = input("Would you like to look up another player? (Y)es or (n)o? ")
                    again = again.lower()

                    if again == "y":
                        print()
                        continue
                    else:
                        print()
                        print("Returning to home page.")
                        print()
                
                else:
                    print("Player not found, try again.")
                    print()
                    continue

            elif position_2023 == "rf":
                p_2023 = ["Ronald Acuna", "Mookie Betts", "George Springer", "Lane Thomas", "Teoscar Hernandez", "Kyle Tucker", "Nick Castellanos", "Anthony Santander", "Fernando Tatis", "Adolis Garcia", "MJ Melendez", "Alex Verdugo", "Seiya Suzuki", "Matt Vierling", "Josh Lowe", "Max Kepler", "Connor Joe", "Michael Conforto", "Jordan Walker", "Kerry Carpenter", "Aaron Judge", "Will Brennan", "Ramon Laureano", "Jesus Sanchez", "Mike Yastrzemski", "Jake Fraley", "Seth Brown", "Jason Heyward", "Gavin Sheets", "Starling Marte", "Kris Bryant", "Will Benson", "Jake McCarthy", "Jake Bauers", "Joshua Palacios", "Oscar Colas", "Henry Davis", "Tyrone Taylor", "Sal Frelick"]
                teams_2023 = ["ATL", "LAD", "TOR", "WSH", "SEA", "HOU", "PHI", "BAL", "SD", "TEX", "KC", "BOS", "CHC", "DET", "TB", "MIN", "PIT", "SF", "STL", "DET", "NYY", "CLE", "CLE", "MIA", "SF", "CIN", "OAK", "LAD", "CWS", "NYM", "COL", "CIN", "AZ", "NYY", "PIT", "CWS", "PIT", "MIL", "MIL"]
                pra_2023 = [.291, .28, .202, .233, .202, .267, .232, .226, .227, .278, .174, .203, .221, .183, .267, .232, .199, .215, .185, .220, .255, .169, .178, .201, .215, .239, .188, .215, .166, .179, .17, .216, .163, .169, .212, .175, .173, .251, .224]
                eba_2023 = [.706, .651, .452, .515, .471, .598, .49, .509, .507, .552, .46, .453, .523, .430, .579, .513, .479, .451, .482, .525, .697, .398, .441, .480, .507, .539, .444, .501, .375, .408, .415, .599, .446, .460, .436, .335, .412, .465, .453]
                bpr_2023 = []
                
                for i in range(len(pra_2023)):
                    bpr_2023 += [pra_2023[i] + eba_2023[i]]
                pra_avg = 0.212
                eba_avg = 0.491
                bpr_avg = 0.703

                pra_sd = statistics.stdev(pra_2023)
                eba_sd = statistics.stdev(eba_2023)
                bpr_sd = statistics.stdev(bpr_2023)

                if name_2023 in p_2023:
                    index = p_2023.index(name_2023)
                    p_team = teams_2023[index]
                    p_pra = pra_2023[index]
                    p_eba = eba_2023[index]
                    p_bpr = bpr_2023[index]
                    p_bpr = float(format(p_bpr, ".3f"))

                    z_score_pra = (p_pra - pra_avg) / pra_sd
                    z_score_eba = (p_eba - eba_avg) / eba_sd
                    z_score_bpr = (p_bpr - bpr_avg) / bpr_sd
    

                    perc_pra = z_to_percentile(z_score_pra)
                    perc_eba = z_to_percentile(z_score_eba)
                    perc_bpr = z_to_percentile(z_score_bpr)

                    g_perc_pra = format(perc_pra, ".2f")
                    g_perc_eba = format(perc_eba, ".2f")
                    g_perc_bpr = format(perc_bpr, ".2f")

                    print()
                    print(name_2023, "--", p_team, "-- Right Field")
                    print("PRA: ", p_pra, " (", g_perc_pra, "%)", sep="")
                    print("EBA: ", p_eba, " (", g_perc_eba, "%)", sep="")
                    print("BPR: ", p_bpr, " (", g_perc_bpr, "%)", sep="")

                    print()
                    again = input("Would you like to look up another player? (Y)es or (n)o? ")
                    again = again.lower()

                    if again == "y":
                        print()
                        continue
                    else:
                        print()
                        print("Returning to home page.")
                        print()
                
                else:
                    print("Player not found, try again.")
                    print()
                    continue
            elif position_2023 == "dh":
                p_2023 = ["Joey Menesses", "Justin Turner", "Shohei Ohtani", "Marcell Ozuna", "Jorge Soler", "Hunter Renfroe", "Bryce Harper", "Brent Rooker", "Mark Canha", "Yordan Alvarez", "Eloy Jimenez", "J.D. Martinez", "Andrew McCutchen", "Harold Ramirez", "Christropher Morel", "Joc Pederson", "Giancarlo Stanton", "Charlie Blackmon", "Brandon Belt", "Miguel Cabrera", "Byron Buxton", "Mitch Garver", "Daniel Vogelbach", "Mike Ford", "Matt Carpenter", "Mark Vientos", "Pavin Smith"]
                teams_2023 = ["WSH", "BOS", "LAA", "ATL", "MIA", "CIN", "PHI", "OAK", "MIL", "HOU", "CWS", "LAD", "PIT", "TB", "CHC", "SF", "NYY", "COL", "TOR", "DET", "MIN", "TEX", "NYM", "SEA", "SD", "NYM", "AZ"]
                pra_2023 = [.224, .254, .255, .243, .2, .182, .247, .19, .201, .288, .196, .273, .182, .263, .247, .224, .19, .215, .191, .138, .213, .221, .213, .199, .186, .137, .215]
                eba_2023 = [.416, .494, .743, .588, .543, .436, .584, .53, .473, .643, .452, .572, .497, .475, .541, .487, .46, .496, .557, .378, .519, .552, .47, .522, .43, .382, .417]
                bpr_2023 = []
                
                for i in range(len(pra_2023)):
                    bpr_2023 += [pra_2023[i] + eba_2023[i]]
                pra_avg = 0.214
                eba_avg = 0.505
                bpr_avg = 0.720

                pra_sd = statistics.stdev(pra_2023)
                eba_sd = statistics.stdev(eba_2023)
                bpr_sd = statistics.stdev(bpr_2023)

                if name_2023 in p_2023:
                    index = p_2023.index(name_2023)
                    p_team = teams_2023[index]
                    p_pra = pra_2023[index]
                    p_eba = eba_2023[index]
                    p_bpr = bpr_2023[index]
                    p_bpr = float(format(p_bpr, ".3f"))

                    z_score_pra = (p_pra - pra_avg) / pra_sd
                    z_score_eba = (p_eba - eba_avg) / eba_sd
                    z_score_bpr = (p_bpr - bpr_avg) / bpr_sd
    

                    perc_pra = z_to_percentile(z_score_pra)
                    perc_eba = z_to_percentile(z_score_eba)
                    perc_bpr = z_to_percentile(z_score_bpr)

                    g_perc_pra = format(perc_pra, ".2f")
                    g_perc_eba = format(perc_eba, ".2f")
                    g_perc_bpr = format(perc_bpr, ".2f")

                    print()
                    print(name_2023, "--", p_team, "-- Designated Hitter")
                    print("PRA: ", p_pra, " (", g_perc_pra, "%)", sep="")
                    print("EBA: ", p_eba, " (", g_perc_eba, "%)", sep="")
                    print("BPR: ", p_bpr, " (", g_perc_bpr, "%)", sep="")

                    print()
                    again = input("Would you like to look up another player? (Y)es or (n)o? ")
                    again = again.lower()

                    if again == "y":
                        print()
                        continue
                    else:
                        print()
                        print("Returning to home page.")
                        print()
                
                else:
                    print("Player not found, try again.")
                    print()
                    continue
            else:
                print("Please enter valid position, try again.")
                print()
                continue 

    elif tab == "5":
    
        print("Input a year you would like to explore into the program and it will give you the season standings and each team's aBPR from that year.")
        def standings_print(numbers):
            
            headers = list(data.keys())
            col_widths = [max(len(str(item)) for item in data[key]) for key in headers]
            header_row = " | ".join(f"{headers[i]:<{col_widths[i]}}" for i in range(len(headers)))
            print(header_row)
            print("-" * len(header_row))

            for i in range(len(data[headers[0]])):
                row = " | ".join(f"{data[key][i]:{col_widths[j]}}" for j, key in enumerate(headers))
                print(row)
        #do the exact same thing as below, just include a prompt for which season you want
        again = "y"
        while again == "y":
            season = input("Enter a season (2021 - 2023): ")
            if season == "2021":
                print("AL WEST")
                data = {"Team": ["HOU", "SEA", "OAK", "LAA", "TEX"],
                        "Wins": [95, 90, 86, 77, 60],
                        "Losses": [67, 72, 76, 85, 102],
                        "aBPR": [13.071, 7.589, 9.697, 7.214, 5.051]}
                standings_print(data)

                print()
                print("AL CENTRAL")
                data = {"Team": ["CWS", "CLE", "DET", "KC", "MIN"],
                    "Wins": [93, 80, 77, 74, 73],
                    "Losses": [69, 82, 85, 88, 89],
                    "aBPR": [11.383, 8.169, 7.008, 6.267, 8.090]}
                standings_print(data)

                print()
                print("AL EAST")
                data = {"Teams": ["TB", "BOS", "NYY", "TOR", "BAL"],
                        "Wins": [100, 92, 92, 91, 52],
                        "Losses": [62, 70, 70, 71, 110],
                        "aBPR": [13.337, 10.302,9.535, 12.560, 3.849]}
                standings_print(data)

                print()
                print("NL WEST")
                data = {"Teams": ["SF", "LAD", "SD", "COL", "AZ"],
                        "Wins": [107, 106, 79, 74, 52],
                        "Losses": [55, 56, 83, 87, 110],
                        "aBPR": [13.451, 14.472, 9.617, 7.477, 5.520]}
                standings_print(data)

                print()
                print("NL CENTRAL")
                data = {"Teams": ["MIL", "STL", "CIN", "CHC", "PIT"],
                        "Wins": [95, 90, 83, 71, 61],
                        "Losses": [67, 72, 79, 91, 101],
                        "aBPR": [10.728, 8.731, 9.415, 6.344, 3.750]}
                standings_print(data)

                print()
                print("NL EAST")
                data = {"Teams": ["ATL", "PHI", "NYM", "MIA", "WSH"],
                        "Wins": [88, 82, 77, 67, 65],
                        "Losses": [73, 80, 85, 95, 97],
                        "aBPR": [11.240, 8.995, 7.370, 6.552, 7.850]}
                standings_print(data)
                print()
                again = input("Would you like to enter a different season? (y)es or (n)o?")
            elif season == "2022":
                print("AL WEST")
                data = {"Teams": ["HOU", "SEA", "LAA", "TEX", "OAK"],
                        "Wins": [106, 90, 73, 68, 60],
                        "Losses": [56, 72, 89, 94, 102],
                        "aBPR": [12.478, 10.395, 7.502, 7.575, 3.560]}
                standings_print(data)
                print()
                print("AL CENTRAL")
                data = {"Teams": ["CLE", "CWS", "MIN", "DET", "KC"],
                        "Wins": [92, 81, 78, 66, 65],
                        "Losses": [70, 81, 84, 96, 97],
                        "aBPR": [10.181, 7.639, 8.671, 4.008, 4.663]}
                standings_print(data)

                print()
                print("AL EAST")
                data = {"Teams": ["NYY", "TOR", "TB", "BAL", "BOS"],
                        "Wins": [99, 92, 86, 83, 78],
                        "Losses": [63, 70, 76, 79, 84],
                        "aBPR": [13.175, 10.908, 9.308, 7.869, 8.124]}
                standings_print(data)

                print()
                print("NL WEST")
                data = {"Teams": ["LAD", "SD", "SF", "AZ", "COL"],
                        "Wins": [111, 89, 81, 74, 68],
                        "Losses": [51, 73, 81, 88, 94],
                        "aBPR": [15.939, 9.556, 8.909, 7.802, 5.646]}
                standings_print(data)

                print()
                print("NL CENTRAL")
                data = {"Teams": ["STL", "MIL", "CHC", "CIN", "PIT"],
                        "Wins": [93, 86, 74, 62, 62],
                        "Losses": [69, 76, 88, 100, 100],
                        "aBPR": [10.772, 10.207, 7.539, 4.623, 3.763]}
                standings_print(data)

                print()
                print("NL EAST")
                data = {"Teams": ["ATL", "NYM", "PHI", "MIA", "WSH"],
                        "Wins": [101, 101, 87, 69, 55],
                        "Losses": [61, 61, 75, 93, 107],
                        "aBPR": [12.035, 11.505, 9.936, 5.962, 3.736]}
                standings_print(data)
                print()
                again = input("Would you like to enter a different season? (y)es or (n)o?")
            elif season == "2023":
                print("AL WEST")
                data = {"Teams": ["HOU", "TEX", "SEA", "LAA", "OAK"],
                        "Wins": [90, 90, 88, 73, 50],
                        "Losses": [72, 72, 74, 89, 112],
                        "aBPR": [11.868, 12.978, 11.541, 7.919, 2.642]}
                standings_print(data)

                print()
                print("AL CENTRAL")
                data = {"Teams": ["MIN", "DET", "CLE", "CWS", "KC"],
                        "Wins": [87, 78, 76, 61, 56],
                        "Losses": [75, 84, 86, 101, 106],
                        "aBPR": [11.780, 7.629, 7.919, 4.498, 5.821]}
                standings_print(data)

                print()
                print("AL EAST")
                data = {"Teams": ["BAL", "TB", "TOR", "NYY", "BOS"],
                        "Wins": [101, 99, 89, 82, 78],
                        "Losses": [61, 63, 73, 80, 84],
                        "aBPR": [11.256, 13.524, 10.580, 8.283, 9.488]}
                standings_print(data)

                print()
                print("NL WEST")
                data = {"Teams": ["LAD", "AZ", "SD", "SF", "COL"],
                        "Wins": [100, 84, 82, 79, 59],
                        "Losses": [62, 78, 80, 83, 103],
                        "aBPR": [14.694, 9.157, 10.743, 8.169, 4.488]}
                standings_print(data)

                print()
                print("NL CENTRAL")
                data = {"Teams": ["MIL", "CHC", "CIN", "PIT", "STL"],
                        "Wins": [92, 83, 82, 76, 71],
                        "Losses": [70, 79, 80, 86, 91],
                        "aBPR": [9.991, 11.507, 9.159, 7.186, 7.422]}
                standings_print(data)

                print()
                print("NL EAST")
                data = {"Teams": ["ATL", "PHI", "MIA", "NYM", "WSH"],
                        "Wins": [104, 90, 84, 75, 71],
                        "Losses": [58, 72, 78, 87, 91],
                        "aBPR": [14.788, 12.014, 7.419, 8.282, 5.790]}

                print()
                again = input("Would you like to enter a different season? (y)es or (n)o?")
                        
                
        
            
    elif tab == "6":
        #2025 projection
        def standings_print(numbers):
            
            headers = list(data.keys())
            col_widths = [max(len(str(item)) for item in data[key]) for key in headers]
            header_row = " | ".join(f"{headers[i]:<{col_widths[i]}}" for i in range(len(headers)))
            print(header_row)
            print("-" * len(header_row))

            for i in range(len(data[headers[0]])):
                row = " | ".join(f"{data[key][i]:{col_widths[j]}}" for j, key in enumerate(headers))
                print(row)
        print()
        print("This tab shows the expected regular season standings for the 2025 season.")
        print()
        print("To project these standings, I started by calculating the aBPR numbers from the 2024 season. Then, I removed all the unrestricted free agents from each team next season, replacing their numbers with the league average at their position to produce a new team aBPR. Next, I performed a z-score to determine the number of wins which correlates to the found aBPR, giving me each team's record. Obviously, there are some flaws to this method including players injured during the 2024 season who will be healthy next year, players who decide to resign with their respective teams, and the possibility that one team has a better free agency than another in terms of signing quality players. Finally, I slighly adjusted the aBPR by factoring in the farm system rank of each team to simulate possible player development")
        print()
        print("AL WEST")
        data = {"Team": ["SEA", "HOU", "OAK", "TEX", "LAA"],
                "Wins": [84, 83, 72, 72, 70],
                "Losses": [78, 79, 90, 90, 92],
                "aBPR": [9.528, 9.340, 7.102, 7.073, 6.062]}
        standings_print(data)
        print()
        print("AL CENTRAL")
        data = {"Team" : ["MIN", "CLE", "KC", "DET", "CWS"],
                "Wins": [97, 89, 87, 81, 49],
                "Losses": [65, 73, 75, 81, 113],
                "aBPR": [12.307, 10.643, 10.327, 9.066, 2.182]}
        standings_print(data)
        print()
        print("AL EAST")
        data = {"Team": ["BOS", "BAL", "NYY", "TB", "TOR"],
                "Wins": [99, 97, 94, 79, 71],
                "Losses": [63, 65, 68, 83, 91],
                "aBPR": [12.822, 12.265, 11.768, 8.551, 6.885]}
        standings_print(data)
        print()
        print("NL WEST")
        data = {"Team": ["LAD", "AZ", "SD", "SF", "COL"],
                "Wins": [101, 90, 83, 78, 60],
                "Losses": [61, 72, 79, 84, 102],
                "aBPR": [13.307, 10.979, 9.353, 8.227, 4.581]}
        standings_print(data)
        print()
        print("NL CENTRAL")
        data = {"Team": ["MIL", "CHC", "CIN", "PIT", "STL"],
                "Wins": [90, 86, 83, 80, 78],
                "Losses": [72, 76, 79, 82, 84],
                "aBPR": [10.932, 9.954, 9.382, 8.704, 8.390]}
        standings_print(data)
        print()
        print("NL EAST")
        data = {"Team": ["PHI", "NYM", "ATL", "WSH", "MIA"],
                "Wins": [94, 89, 82, 77, 61],
                "Losses": [68, 73, 80, 85, 101],
                "aBPR": [11.764, 10.613, 9.095, 8.139, 4.620]}
        standings_print(data)
        print()
        
                                
    elif tab == "7":
        #exit
        print()
        print("Thank you and Goodbye")
        break
    else:
        print()
        print("Invalid Entry, try again")
        print()
        
