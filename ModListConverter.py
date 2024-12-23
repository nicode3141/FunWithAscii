def covertString(input):
    lines = input.split('\n')
    cleaned_lines = []

    for line in lines:
        parts = line.split(' ')
        cleaned_parts = []
        skip = False

        for part in parts:
            if part == '(by':
                skip = True
            elif skip and part.endswith(')'):
                skip = False
            elif not skip:
                cleaned_parts.append(part)

        cleaned_line = ' '.join(cleaned_parts)
        cleaned_lines.append(cleaned_line.strip())

    return '\n'.join(cleaned_lines)


string = """Chisel (by tterrag1098)
FTB Utilities (Forge) (by FTB)
Extra Utilities (by RWTema)
Actually Additions (by Ellpeck)
MCMultiPart (by amadornes)
NuclearCraft (by tomdodd4598)
BetterFps (by Guichaguri)
MalisisCore (by Ordinastie)
Quick Leaf Decay (by Lumien231)
Industrial Wires (by malte0811)
Chisels & Bits - For Forge (by AlgorithmX2)
Morpheus (by Quetzi)
Just Enough Dimensions (by masady)
Aroma1997Core (by Aroma1997)
Cooking for Blockheads (by BlayTheNinth)
Thermal Dynamics (by TeamCoFH)
MalisisDoors (by Ordinastie)
Industrial Foregoing (by Buuz135)
JEI Integration (by SnowShock35)
Immersive Petroleum (by Flaxbeard)
AutoRegLib (by Vazkii)
Waystones (by BlayTheNinth)
CompatLayer (by McJty)
ExtraCells2 (by Forge_User_54797008)
Draconic Evolution (by brandon3055)
CB Multipart (by covers1624)
Mixin 0.7-0.8 Compatibility (by NotStirred)
SuperMartijn642's Core Lib (by SuperMartijn642)
Cyclic (by Lothrazar)
Tinkers Construct (by mDiyo)
Tesla Core Lib (by face_of_cat)
ConnectedTexturesMod (by tterrag1098)
Trash Cans (by SuperMartijn642)
Inventory Tweaks [1.12 only] (by JimeoWan)
Ore Excavation (by Funwayguy)
AE2 Wireless Terminal Library (by TheRealp455w0rd)
Wireless Crafting Terminal (by TheRealp455w0rd)
FTB Library (Forge) (Legacy) (by FTB)
Brandon's Core (by brandon3055)
Doomlike Dungeons (by JaredBGreat)
Biomes O' Plenty (by Forstride)
Storage Drawers (by Texelsaur)
Woot (by Ipsis)
Mantle (by mDiyo)
CoFH Core (by TeamCoFH)
RFTools Control (by McJty)
PTRLib (by RazzleberryFox)
FTB Backups (Forge) (by FTB)
Thaumcraft (by Azanor13)
Default World Generator (port) (by ezterry)
Controlling (by Jaredlll08)
Cucumber Library (by BlakeBr0)
RFTools (by McJty)
Iron Chests (by ProgWML6)
Tomb Many Graves 2 (by M4thG33k)
Mekanism Tools (by bradyaidanc)
Immersive Engineering (by BluSunrize)
AE2 Stuff (by bdew)
BdLib (by bdew)
Thermal Foundation (by TeamCoFH)
Phosphor (Forge) (by JellySquid)
EnderCore (by tterrag1098)
Cyclops Core (by kroeser)
Not Enough Wands (by romelo333)
Baubles (by Azanor13)
Techguns (by pWn3d_1337)
CoFH World (by TeamCoFH)
ValkyrieLib (by ValkyrieofNight)
Crafting Tweaks (by BlayTheNinth)
Ceramics (by KnightMiner)
Aroma1997s Dimensional World (by Aroma1997)
Ender Storage 1.8.+ (by covers1624)
Ender IO (by crazypants_mc_the_second)
ZeroCore 2 (by ZeroNoRyouki)
MysticalLib (by Noobanidus)
CraftTweaker (by Jaredlll08)
BiblioCraft (by Nuchaz)
Botania (by Vazkii)
Clumps (by Jaredlll08)
Just Enough Items (JEI) (by mezz)
Better Builder's Wands (by Portablejim)
Dynamic Transport (by Tarig)
Default Options (by BlayTheNinth)
JourneyMap (by techbrew)
p455w0rd's Library (by TheRealp455w0rd)
Shadowfacts' Forgelin (by ShadowfactsDev)
Mekanism (by bradyaidanc)
Mystical Agriculture (by BlakeBr0)
Building Gadgets (by Direwolf20)
Chameleon (by Texelsaur)
Storage Drawers Extras (by Texelsaur)
Environmental Tech (by ValkyrieofNight)
RFTools Power (by McJty)
Mekanism Generators (by bradyaidanc)
The One Probe (by McJty)
Mystical Agradditions (by BlakeBr0)
Pam's HarvestCraft (by pamharvestcraft)
RFTools Dimensions (by McJty)
OpenComputers (by Sangar)
CodeChicken Lib 1.8.+ (by covers1624)
Blockcraftery (by EpicSquid315)
Redstone Flux (by TeamCoFH)
Quark (by Vazkii)
Thermal Expansion (by TeamCoFH)
McJtyLib (by McJty)
Applied Energistics 2 (by thetechnici4n)"""

print(covertString(string))
