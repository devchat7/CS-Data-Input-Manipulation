# PE02 - OOP and Comprehensions
# only the following imports are allowed
import copy

class Podcast:

    def __init__(self, name, genre, total_episodes, host_names):
        """
        Question 1a
            Complete the __init__ method by passing in parameters and assign the parameters to the
            corresponding attributes. __init__ should take in the full podcast name, genre, total 
            number of episodes, and a list of host names.

            Example:
                >>> pod0 = Podcast("The Joe Rogan Experience", "Comedy", 1764, ['Joe Rogan'])
        """
        self.name = name 
        self.genre = genre
        self.total_episodes = total_episodes
        self.host_names = host_names

    def __eq__(self, other):
        """
        Question 1b
            Complete the __eq__ method. Two Podcast objects are equal if and only if they share the
            same name and number of episodes.
            Example:
                >>> pod1 = Podcast("Crime Junkies", "True Crime", 453, ['Ashley Flowers', 'Brit Prawat'])
                >>> pod2 = Podcast("Crime Junkies", "Science Fiction", 453, ['audiochuck'])
                >>> pod1 == pod2
                True
        """
        return self.name == other.name and self.total_episodes == other.total_episodes


    def __lt__(self, other):
        """
        Question 1c
            Complete the __lt__ method. A Podcast object is less than another if it has less episodes.

            Example:
                >>> pod3 = Podcast("Freakonomics Radio", "Education", 490, ['Stephen J. Dubner'])
                >>> pod4 = Podcast("Dear Hank & John", "Philosophy", 316, ['Hank Green', 'John Green'])
                >>> pod3 < pod4
                False
        """
        return self.total_episodes < other.total_episodes

    def __repr__(self):
        """
        Question 1d
            Complete the __repr__ method. Calling or printing a Podcast object
            should be represented as the following string:
                'The "{name}" podcast, hosted by {elements of host_names seperated by "and"}, has 
                {total_episodes} episodes and is in the {genre} category.'

            Example:
                >>> pod5 = Podcast("The Journal", "News", 847, ['Kate Linebaugh', 'Ryan Knutson'])
                >>> pod5
                'The "The Journal" podcast, hosted by Kate Linebaugh and Ryan Knutson, has 
                847 episodes and is in the News category.'
        """
        return f"The \"{self.name}\" podcast, hosted by {' and '.join(self.host_names)}, has {self.total_episodes} episodes and is in the {self.genre} category."

########################################################################
#                                                                      #
# Questions 2 to 4 MUST be answered in ONE line using comprehensions.  #
#                                                                      #
########################################################################

def category_podcast(podcast_list, category):
    """
    Question 2 (solution must be written in one line)
        Write a function that passes in a list of Podcast objects and a preferred podcast genre.
        Return a list of Podcast objects' name that belongs to that genre.
        You must use a list comprehension!

        Example:
            >>> pod1 = Podcast("Crime Junkies", "True Crime", 512, ['Ashley Flowers', 'Brit Prawat'])
            >>> pod2 = Podcast("Psychedelics for the Win", "Business", 390, ['Aspen Ideas'])
            >>> pod3 = Podcast("Exponential Organization", "Business", 17, ['Salim Ismail', 'Yuri van Geest', 'Michael S. Malone'])
            >>> pod_list = [pod1, pod2, pod3]
            >>> category_podcast(pod_list, 'Business')
            ["Psychedelics for the Win", "Exponential Organization"]
    """
    return [x.name for x in podcast_list if x.genre == category]

def assign_logos(logos, podcast_list):
    """
    Question 3 (solution must be written in one line)
        Write a function that takes in a list of strings representing podcast logos and a
        corresponding list of Podcast objects. Your function should return a dictionary where
        the key is the podcast name and the value is the logo.
        Make sure to use dictionary comprehension!!!

        Example:
            >>> logos = ["Wrench", "Race Helmet", "Flat Tire"]
            >>> cartalk = Podcast("Car Talk", "Comedy", 2206, ["Tom Magliozzi", "Ray Magliozzi"])
            >>> pastgas = Podcast("Past Gas",  "Education", 125, ["Nolan John Sykes", "James Pumphrey", "Joe Weber"])
            >>> smokingtire = Podcast("The Smoking Tire", "Comedy", 600, ["Matt Farah", "Zack Klapman"])
            >>> podcast_list = [cartalk, pastgas, smokingtire]
            >>> assign_logos(logos, podcast_list)
            {"Car Talk": "Wrench", "Past Gas": "Race Helmet", "The Smoking Tire": "Flat Tire"}
    """
    return {x.name : y for x,y in list(zip(podcast_list,logos))}


def bad_host(podcast, removal_host):
    """
    Question 4 (solution must be written in one line)
        You are a podcast manager. One of the hosts on your podcast is awful, and offers poor commentary.

        You want to remove this bad host from the show. This function should
        remove the host's name in the variable 'removal_host' from the Podcast object's host_names attribute. 
        This method alters the Podcast object attribute and returns nothing. 

        Example:
            >>> pod1 = Podcast("Crime Junkies", "True Crime", 453, ['Ashley Flowers', 'Brit Prawat'])
            >>> bad_host(pod1, 'Brit Prawat')
            >>> print(pod1.host_names)
            ['Ashley Flowers']
    """
    podcast.host_names = [x for x in podcast.host_names if x != removal_host]
    

def episode_updater(original_podcasts):
    """
    Question 5 (solution can be written using multiple lines)
        You are currently working as a Spotify intern. As your first project, your intern manager
        explains that their automated podcast update system has gone offline and tasks you with the
        job of manually updating the number of episodes for some podcasts. He provides you with a
        list of Podcast objects (`original_podcasts`) that requires their episode count to be incremented
        by 1. 

        Make a deep copy of `original_podcasts`, and then for each Podcast object in the newly created
        deep copy, increment the total_episodes by 1 episode. Once you have updated each Podcast
        object, add all the updated Podcast objects to a new list and return the list.

        Example:
            >>> pod1 = Podcast("Crime Junkies", "True Crime", 453, ['Ashley Flowers', 'Brit Prawat'])
            >>> pod2 = Podcast("Crime Junkies", "Science Fiction", 453, ['audiochuck'])
            >>> pod3 = Podcast("Freakonomics Radio", "Education", 490, ['Stephen J. Dubner'])
            >>> original_podcasts = [pod1, pod2, pod3]
            >>> new_podcasts = episode_updater(original_podcasts)
            >>> original_podcasts[0].total_episodes == new_podcasts[0].total_episodes
            False
            >>> original_podcasts[0].total_episodes + 1 == new_podcasts[0].total_episodes
            True
            >>> original_podcasts[1].total_episodes + 1 == new_podcasts[1].total_episodes
            True
            >>> original_podcasts[2].total_episodes + 1 == new_podcasts[2].total_episodes
            True
    """
    i = 0
    new_podcast = copy.deepcopy(original_podcasts)
    episode_list = [x.total_episodes + 1 for x in new_podcast]
    for y in episode_list :
        new_podcast[i].total_episodes = episode_list[i]
        i += 1
    return(new_podcast)
    

if __name__ == "__main__" :
    ### Test Class Initialization ###

    ### test __init__ method ###
    pod0 = Podcast("The Joe Rogan Experience", "Comedy", 1764, ['Joe Rogan'])

    ### test __eq__ method ###
    pod1 = Podcast("Crime Junkies", "True Crime", 453, ['Ashley Flowers', 'Brit Prawat'])
    pod2 = Podcast("Crime Junkies", "Science Fiction", 453, ['audiochuck'])
    #print(pod1 == pod2)

    ### test __lt__ method ###
    pod3 = Podcast("Freakonomics Radio", "Education", 490, ['Stephen J. Dubner'])
    pod4 = Podcast("Dear Hank & John", "Philosophy", 316, ['Hank Green', 'John Green'])
    #print(pod3 < pod4)

    ### test __repr__ method ###
    pod5 = Podcast("The Journal", "News", 847, ['Kate Linebaugh', 'Ryan Knutson'])
    print(pod5)

    ##################################################################################
    #    When testing Questions 2 - 5, leave pod0 -> pod5 from above uncommented.    #
    ##################################################################################
    
    ### Question 2 ####
    p1 = Podcast("Crime Junkies", "True Crime", 512, ['Ashley Flowers', 'Brit Prawat'])
    p2 = Podcast("Psychedelics for the Win", "Business", 390, ['Aspen Ideas'])
    p3 = Podcast("Exponential Organization", "Business", 17, ['Salim Ismail', 'Yuri van Geest', 'Michael S. Malone'])
    pod_list = [p1, p2, p3]
    #print(category_podcast(pod_list,'Business'))
    p_list2 = [pod1,pod2,pod4]
    #print(category_podcast(p_list2,'Science Fiction'))

    ### Question 3 ###
    logos = ["Wrench", "Race Helmet", "Flat Tire"]
    cartalk = Podcast("Car Talk", "Comedy", 2206, ["Tom Magliozzi", "Ray Magliozzi"])
    pastgas = Podcast("Past Gas",  "Education", 125, ["Nolan John Sykes", "James Pumphrey", "Joe Weber"])
    smokingtire = Podcast("The Smoking Tire", "Comedy", 600, ["Matt Farah", "Zack Klapman"])
    podcast_list = [cartalk, pastgas, smokingtire]
    #print(assign_logos(logos, podcast_list))

    ## Question 4 ###
    #print(pod1.host_names)
    #bad_host(pod1, 'Brit Prawat')
    #print(pod1.host_names)
    

    ### Question 5 ###
    original_podcasts = [pod1, pod2, pod3]
    new_podcasts = episode_updater(original_podcasts)
    print(original_podcasts[0].total_episodes == new_podcasts[0].total_episodes)
    print(original_podcasts[0].total_episodes + 1 == new_podcasts[0].total_episodes)
    print(original_podcasts[1].total_episodes + 1 == new_podcasts[1].total_episodes)
    print(original_podcasts[2].total_episodes + 1 == new_podcasts[2].total_episodes)