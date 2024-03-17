
def anti_shuffle(s):
    """
    Ek function likho jo ek string leta hai aur uska ordered version return karta hai.
    Ordered version of string, woh string hoti hai jahan saare words (space se separated)
    ko ek naye word se replace kiya jata hai jahan saare characters ko 
    unke ascii value ke basis pe ascending order mein arrange kiya jata hai.
    Dhyan do: Aapko words aur blank spaces ki order sentence mein maintain karni chahiye.

    Jaise ki:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello!!!Wdlor'
    """
    aList = re.split("\s", s)
    aList.sort(key=abs)
    return''.join(aList)

#TODO:
#Bharat Mandi-chandini Vyaya hai ke aapni jot hai ki, neh rekha se bhi hai
#Bharat Mandi-chandini Vyaya hai ki, neha aur neh ehi karne ke bhi hai ki, aur neh ehi nahi ke karne ke bhi hai ki

#Possible inputs to check order for
#
#('Sajal', 'Rajiv', 'Darshan', 'Sagar', 'Meghnad', 'Jinjali', 'Shivanand', 'Abhi', 'Yazhang', 'Rajkumar', 'Chamika', 'Saradhi')

#s2 = 'Sajal Rajiv Darshan Khanjana Sagar Shivanand Shahvnjania Jinjali Kumri Mohat Nati Bharadani Chambir Singh Sharma Sajanayaji Abhishek Rajayarangaya Chandan Vasudha Rajendra Madhaja Chitrakendra Vasudha Lakshman Das Katakandari Kunal Pradhan Vivek Dasti Anirudh Pradhan Bibi Padavar Pradhan Anurag Pad