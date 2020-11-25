# family-tree

## Problem
1. Build a family tree
2. Monogamous relationship
3. Traverse based on relationships
4. Add new members to the family

## Assumption / Limitations
1. No Duplicate names
2. Names cannot have spaces

## Commands
* ADD_CHILD <Child's Mother>  <Child's name> <Gender> 
* ADD_SPOUSE <Member's Name> <Spouse Name>
* GET_RELATIONSHIP <Member's name> <Relationship Name>
** Relationship:
*** Spouse
*** Daughters
*** Siblings
*** Sons
*** Brothers
*** Sisters
*** Paternal-Uncles
*** Paternal-Aunts
*** Maternal-Uncles
*** Maternal-Aunts
*** Sisters-In-Law
*** Brothers-In-Law



## Solution

### Data Structure
1. Dictionary of members with 'Name' as the key.
2. Each member of is a dictionary with properties { Spouse: String, Male: Boolean, Mother: String, Children: Array }
