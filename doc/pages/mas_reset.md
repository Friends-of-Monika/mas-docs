## Functions

### def ch30_reset(priority=0)

decorator that marks function to run as part of ch30_reset.

**Parameters:**
- `func` &mdash; function to register
- `priority` &mdash; priority to run function Default: 0 PLEASE USE POSITIVE PRIORITIES. If you need to slip something between existing reset code, be mindful of where you plugin your reset code. Take a look at the reset functions below for the correct placement.


---### def ch30_reset(priority=0)

decorator that marks function to run as part of ch30_reset.

**Parameters:**
- `func` &mdash; function to register
- `priority` &mdash; priority to run function Default: 0 PLEASE USE POSITIVE PRIORITIES. If you need to slip something between existing reset code, be mindful of where you plugin your reset code. Take a look at the reset functions below for the correct placement.


---### def start()

Reset code that should always be first

**Decorators:**
- `@ch30_reset(-980)`


---### def xp()

Runs reset code specific for xp stuff

**Decorators:**
- `@ch30_reset(-960)`


---### def name_eggs()

Runs reset code specific for name eggs

**Decorators:**
- `@ch30_reset(-940)`


---### def topic_lists()

Runs reset code specific for topic lists

**Decorators:**
- `@ch30_reset(-920)`


---### def rpy_file_check()

Runs reset code specific for the rpy file check

**Decorators:**
- `@ch30_reset(-900)`


---### def games()

Runs reset code specific for games

**Decorators:**
- `@ch30_reset(-880)`


---### def sprites()

Runs reset code for sprites

**Decorators:**
- `@ch30_reset(-860)`


---### def random_chatter()

Runs reset code for random chatter

**Decorators:**
- `@ch30_reset(-840)`


---### def returned_home()

Runs reset code for returned home

**Decorators:**
- `@ch30_reset(-820)`


---### def playtime()

Runs reset code for playtime

**Decorators:**
- `@ch30_reset(-800)`


---### def affection()

Runs reset code for affection

**Decorators:**
- `@ch30_reset(-780)`


---### def deco()

Runs reset code for deco

**Decorators:**
- `@ch30_reset(-760)`


---### def farewells()

Runs reset code for farewells

**Decorators:**
- `@ch30_reset(-740)`


---### def file_reactions()

Runs reset code for file reactions

**Decorators:**
- `@ch30_reset(-720)`


---### def events()

Runs reset code for general events + events list stuff

**Decorators:**
- `@ch30_reset(-700)`


---### def songs()

Runs reset code for songs

**Decorators:**
- `@ch30_reset(-680)`


---### def holidays()

Runs reset code for holidays that do not fall under the other categories.

**Decorators:**
- `@ch30_reset(-660)`


---### def backgrounds()

Runs reset code for backgrounds

**Decorators:**
- `@ch30_reset(-640)`


---### def window_reactions()

Runs reset code for window reactions

**Decorators:**
- `@ch30_reset(-620)`


---### def islands()

Runs reset code for islands

**Decorators:**
- `@ch30_reset(-600)`


---### def bath_cleanup()

Cleanup code for bath stuff

**Decorators:**
- `@ch30_reset(-580)`


---### def chr_removal()

Remove .chr files in the characters folder

**Decorators:**
- `@ch30_reset(-560)`


---### def backups()

Runs reset for backup code

**Decorators:**
- `@ch30_reset(-560)`


---### def final()

Runs reset code that should run after everythign else

---### def start()

Reset code that should always be first

**Decorators:**
- `@ch30_reset(-980)`


---### def xp()

Runs reset code specific for xp stuff

**Decorators:**
- `@ch30_reset(-960)`


---### def name_eggs()

Runs reset code specific for name eggs

**Decorators:**
- `@ch30_reset(-940)`


---### def topic_lists()

Runs reset code specific for topic lists

**Decorators:**
- `@ch30_reset(-920)`


---### def rpy_file_check()

Runs reset code specific for the rpy file check

**Decorators:**
- `@ch30_reset(-900)`


---### def games()

Runs reset code specific for games

**Decorators:**
- `@ch30_reset(-880)`


---### def sprites()

Runs reset code for sprites

**Decorators:**
- `@ch30_reset(-860)`


---### def random_chatter()

Runs reset code for random chatter

**Decorators:**
- `@ch30_reset(-840)`


---### def returned_home()

Runs reset code for returned home

**Decorators:**
- `@ch30_reset(-820)`


---### def playtime()

Runs reset code for playtime

**Decorators:**
- `@ch30_reset(-800)`


---### def affection()

Runs reset code for affection

**Decorators:**
- `@ch30_reset(-780)`


---### def deco()

Runs reset code for deco

**Decorators:**
- `@ch30_reset(-760)`


---### def farewells()

Runs reset code for farewells

**Decorators:**
- `@ch30_reset(-740)`


---### def file_reactions()

Runs reset code for file reactions

**Decorators:**
- `@ch30_reset(-720)`


---### def events()

Runs reset code for general events + events list stuff

**Decorators:**
- `@ch30_reset(-700)`


---### def songs()

Runs reset code for songs

**Decorators:**
- `@ch30_reset(-680)`


---### def holidays()

Runs reset code for holidays that do not fall under the other categories.

**Decorators:**
- `@ch30_reset(-660)`


---### def backgrounds()

Runs reset code for backgrounds

**Decorators:**
- `@ch30_reset(-640)`


---### def window_reactions()

Runs reset code for window reactions

**Decorators:**
- `@ch30_reset(-620)`


---### def islands()

Runs reset code for islands

**Decorators:**
- `@ch30_reset(-600)`


---### def bath_cleanup()

Cleanup code for bath stuff

**Decorators:**
- `@ch30_reset(-580)`


---### def chr_removal()

Remove .chr files in the characters folder

**Decorators:**
- `@ch30_reset(-560)`


---### def backups()

Runs reset for backup code

**Decorators:**
- `@ch30_reset(-560)`


---### def final()

Runs reset code that should run after everythign else

---### Internal functions

> [!CAUTION]
> These functions are *internal* and are not recommended for use.

#### def _sprites_init()

Runs reset code for initializing sprites

---#### def _sprites_fixes()

Runs reset code for fixing sprite issues

---#### def _sprites_setup()

Runs other sprite setup that is not init or fixes

---#### def _deco_bday()

Runs reset code for bday deco

---#### def _deco_d25()

Runs reset code for d25 deco

---#### def _deco_o31()

Runs reset code for o31 deco

---#### def _sprites_init()

Runs reset code for initializing sprites

---#### def _sprites_fixes()

Runs reset code for fixing sprite issues

---#### def _sprites_setup()

Runs other sprite setup that is not init or fixes

---#### def _deco_bday()

Runs reset code for bday deco

---#### def _deco_d25()

Runs reset code for d25 deco

---#### def _deco_o31()

Runs reset code for o31 deco

---