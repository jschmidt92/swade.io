interface NpcCreate {
    [key: string]: any
    name: string
    race: string
    gender: string
    charisma: number
    pace: number
    parry: number
    toughness: number
    attributes: Record<string, string>
    skills: Record<string, string>
    hindrances: string
    edges: string
    ammo: number
    money: number
  }
  
  interface NpcList {
    id: number
    name: string
    race: string
    gender: string
    damage: Record<string, number | string>
  }
  
  interface NpcUpdate extends Partial<Omit<NpcCreate, 'attributes' | 'skills' | 'damage'>> {
    id: number
    gear?: NestedGear[]
    cyberware?: Cyberware[]
    powers?: Power[]
    weapons?: NestedWeapon[]
  }
  
  interface NpcView extends NpcCreate {
    id: number
    gear: NestedGear[]
    cyberware: Cyberware[]
    powers: Power[]
    weapons: NestedWeapon[]
  }
  
  interface Cyberware {
    id: number
    name: string
    strain: number
    effect: string
    price: number
    notes: string
  }
  
  interface Gear {
    id: number
    name: string
    min_str: string
    wt: number
    cost: number
    notes: string
  }
  
  interface Power {
    id: number
    name: string
    pp: string
    range: string
    duration: string
    effect: string
    notes: string
  }
  
  interface NestedGear {
    gear: {
      id: number
      name: string
      min_str: string
      wt: number
      cost: number
      notes: string
    }
    quantity: number
  }
  
  interface NestedWeapon {
    weapon: {
      id: number
      name: string
      range: string
      damage: string
      rof: number
      shots: number
      min_str: string
      wt: number
      cost: number
      notes: string
    }
    quantity: number
  }
  
  interface Weapon {
    id: number
    name: string
    range: string
    damage: string
    rof: number
    shots: number
    min_str: string
    wt: number
    cost: number
    notes: string
  }
  
  interface Attribute {
    name: string
    value: string
    items?: Dictionary[]
  }
  
  interface Dictionary {
    name: string
    value: string
  }
  
  interface Skill {
    name: string
    value: string
    items?: Dictionary[]
  }
  
  interface FormNpcCreate extends Omit<NpcCreate, 'attributes' | 'skills' | 'damage'> {
    attributes: Record<string, string>
    skills: Record<string, string>
    damage: string
  }
  
  enum Gender {
    male = 'Male',
    female = 'Female'
  }
  
  enum Race {
    android = 'Android',
    anklebiter = 'Anklebiter',
    angler = 'Angler',
    apex = 'A-Pex',
    aquarian = 'Aquarian',
    aurax = 'Aurax',
    avion = 'Avion',
    behemoth = 'Behemoth',
    bloodwing = 'Bloodwing',
    boomer = 'Boomer',
    colemata = 'Colemata',
    construct = 'Contruct',
    deader = 'Deader',
    deathcrawler = 'Death Crawler (Swarm)',
    drake = 'Drake',
    dwarf = 'Dwarf',
    elf = 'Elf',
    floran = 'Floran',
    halfelve = 'Half-Elve',
    halffolk = 'Half-Folk',
    human = 'Human',
    hunter = 'Hunter',
    insectoid = 'Insectoid',
    kalian = 'Kalian',
    krok = 'Krok',
    krokgiant = 'Krok, Giant',
    lightningdarter = 'Lightning Darter (Swarm)',
    lacerauns = 'Lacerauns',
    mauler = 'Mauler',
    rakashan = 'Rakashan',
    ravager = 'Ravager',
    robot = 'Robot',
    sailfin = 'Sailfin',
    saurian = 'Saurian',
    scrat = 'Scrat',
    scuteboar = 'Scute Boar',
    serran = 'Serran',
    scylla = 'Scylla',
    scyllagiant = 'Scylla Giant',
    sirencreeper = 'Siren Creeper',
    spitter = 'Spitter',
    yeti = 'Yeti'
  }

  enum Faction {
    unknown = 'Unknown',
    neutral = 'Neutral',
    friendly = 'Friendly',
    enemy = 'Enemy'
  }
  
  export type {
    Attribute,
    NpcCreate,
    NpcList,
    NpcUpdate,
    NpcView,
    Dictionary,
    FormNpcCreate,
    Gear,
    Skill,
    Weapon
  }
  export { Faction, Gender, Race }
  