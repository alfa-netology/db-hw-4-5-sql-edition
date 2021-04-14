data = {
    'drop_tables': 'DROP TABLE IF EXISTS '
                   'Albums,'
                   'Genres,'
                   'Performers,'
                   'PerformerAlbum,'
                   'PerformerGenre,'
                   'Tracks,'
                   'Collections,'
                   'TrackCollection'
                   ' CASCADE;',

    'create_tables': 'CREATE TABLE Performers( '
                     'id serial PRIMARY KEY,'
                     'name VARCHAR(150) NOT NULL);'
                     ''
                     'CREATE TABLE Albums('
                     'id serial PRIMARY KEY,'
                     'title VARCHAR(200) NOT NULL,'
                     'year NUMERIC(4,0) NOT NULL);'
                     ''
                     'CREATE TABLE PerformerAlbum('
                     'performer_id INTEGER REFERENCES Performers(id),'
                     'album_id INTEGER REFERENCES Albums(id),'
                     'CONSTRAINT pa_pk PRIMARY KEY (performer_id, album_id));'
                     ''
                     'CREATE TABLE Genres('
                     'id serial PRIMARY KEY,'
                     'title VARCHAR(100) NOT NULL);'
                     ''
                     'CREATE TABLE PerformerGenre('
                     'performer_id INTEGER REFERENCES Performers(id),'
                     'genre_id INTEGER REFERENCES Genres(id),'
                     'CONSTRAINT pg_pk PRIMARY KEY (performer_id, genre_id));'
                     ''
                     'CREATE TABLE Tracks('
                     'id serial PRIMARY KEY,'
                     'title TEXT NOT NULL,'
                     'duration INTEGER NOT NULL,'
                     'album_id INTEGER NOT NULL REFERENCES Albums(id));'
                     ''
                     'CREATE TABLE Collections('
                     'id serial PRIMARY KEY,'
                     'title VARCHAR(200) NOT NULL,'
                     'year NUMERIC(4,0) NOT NULL);'
                     ''
                     'CREATE TABLE TrackCollection('
                     'track_id INTEGER REFERENCES Tracks(id),'
                     'collection_id INTEGER NOT NULL REFERENCES Collections(id),'
                     'CONSTRAINT tc_pk PRIMARY KEY (track_id, collection_id));'
}

performers_data = {
    "The XX": {
        "albums": [
            {
                "id": "2118357",
                "title": "xx",
                "year": "2009",
                "genre": "Pop",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Intro",
                        "duration": "127920"
                    },
                    {
                        "number": "2",
                        "title": "VCR",
                        "duration": "177093"
                    },
                    {
                        "number": "3",
                        "title": "Crystalised",
                        "duration": "201946"
                    },
                    {
                        "number": "4",
                        "title": "Islands",
                        "duration": "160720"
                    },
                    {
                        "number": "5",
                        "title": "Heart Skipped a Beat",
                        "duration": "242266"
                    },
                    {
                        "number": "6",
                        "title": "Fantasy",
                        "duration": "158240"
                    },
                    {
                        "number": "7",
                        "title": "Shelter",
                        "duration": "270240"
                    },
                    {
                        "number": "8",
                        "title": "Basic Space",
                        "duration": "188120"
                    },
                    {
                        "number": "9",
                        "title": "Infinity",
                        "duration": "313386"
                    },
                    {
                        "number": "10",
                        "title": "Night Time",
                        "duration": "216853"
                    },
                    {
                        "number": "11",
                        "title": "Stars",
                        "duration": "262640"
                    }
                ]
            },
            {
                "id": "2120659",
                "title": "Coexist",
                "year": "2012",
                "genre": "Pop",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Angels",
                        "duration": "172000"
                    },
                    {
                        "number": "2",
                        "title": "Chained",
                        "duration": "168000"
                    },
                    {
                        "number": "3",
                        "title": "Fiction",
                        "duration": "178000"
                    },
                    {
                        "number": "4",
                        "title": "Try",
                        "duration": "196000"
                    },
                    {
                        "number": "5",
                        "title": "Reunion",
                        "duration": "238000"
                    },
                    {
                        "number": "6",
                        "title": "Sunset",
                        "duration": "219000"
                    },
                    {
                        "number": "7",
                        "title": "Missing",
                        "duration": "215000"
                    },
                    {
                        "number": "8",
                        "title": "Tides",
                        "duration": "182000"
                    },
                    {
                        "number": "9",
                        "title": "Unfold",
                        "duration": "184000"
                    },
                    {
                        "number": "10",
                        "title": "Swept Away",
                        "duration": "300000"
                    },
                    {
                        "number": "11",
                        "title": "Our Song",
                        "duration": "195000"
                    }
                ]
            },
            {
                "id": "2238427",
                "title": "iTunes Live From SoHo",
                "year": "2010",
                "genre": "Pop",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Intro (live)",
                        "duration": "170000"
                    },
                    {
                        "number": "2",
                        "title": "Islands (live)",
                        "duration": "167000"
                    },
                    {
                        "number": "3",
                        "title": "Fantasy (live)",
                        "duration": "146000"
                    },
                    {
                        "number": "4",
                        "title": "Shelter (live)",
                        "duration": "254000"
                    },
                    {
                        "number": "5",
                        "title": "Night Time (live)",
                        "duration": "267000"
                    }
                ]
            },
            {
                "id": "2238429",
                "title": "Basic Space",
                "year": "2009",
                "genre": "Pop",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Basic Space",
                        "duration": "188065"
                    },
                    {
                        "number": "2",
                        "title": "Blood Red Moon (demo)",
                        "duration": "133251"
                    }
                ]
            },
            {
                "id": "2276253",
                "title": "I See You",
                "year": "2017",
                "genre": "Pop",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Dangerous",
                        "duration": "250000"
                    },
                    {
                        "number": "2",
                        "title": "Say Something Loving",
                        "duration": "238000"
                    },
                    {
                        "number": "3",
                        "title": "Lips",
                        "duration": "200000"
                    },
                    {
                        "number": "4",
                        "title": "A Violent Noise",
                        "duration": "227000"
                    },
                    {
                        "number": "5",
                        "title": "Performance",
                        "duration": "246000"
                    },
                    {
                        "number": "6",
                        "title": "Replica",
                        "duration": "249000"
                    },
                    {
                        "number": "7",
                        "title": "Brave for You",
                        "duration": "253000"
                    },
                    {
                        "number": "8",
                        "title": "On Hold",
                        "duration": "224000"
                    },
                    {
                        "number": "9",
                        "title": "I Dare You",
                        "duration": "233000"
                    },
                    {
                        "number": "10",
                        "title": "Test Me",
                        "duration": "235000"
                    }
                ]
            },
            {
                "id": "2301605",
                "title": "Tour 7\"",
                "year": "2010",
                "genre": "",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Do You Mind?",
                        "duration": "221000"
                    },
                    {
                        "number": "2",
                        "title": "Hot Like Fire",
                        "duration": "205000"
                    },
                    {
                        "number": "3",
                        "title": "Teardrops",
                        "duration": "232000"
                    },
                    {
                        "number": "4",
                        "title": "Blood Red Moon",
                        "duration": "130000"
                    }
                ]
            }
        ]
    },
    "Daft Punk": {
        "albums": [
            {
                "id": "2112973",
                "title": "Homework",
                "year": "1997",
                "genre": "House",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Daftendirekt",
                        "duration": "164640"
                    },
                    {
                        "number": "2",
                        "title": "WDPK 83.7 FM",
                        "duration": "28293"
                    },
                    {
                        "number": "3",
                        "title": "Revolution 909",
                        "duration": "326506"
                    },
                    {
                        "number": "4",
                        "title": "Da Funk",
                        "duration": "329560"
                    },
                    {
                        "number": "5",
                        "title": "Ph\u0153nix",
                        "duration": "297133"
                    },
                    {
                        "number": "6",
                        "title": "Fresh",
                        "duration": "244400"
                    },
                    {
                        "number": "7",
                        "title": "Around the World",
                        "duration": "429506"
                    },
                    {
                        "number": "8",
                        "title": "Rollin' & Scratchin'",
                        "duration": "447533"
                    },
                    {
                        "number": "9",
                        "title": "Teachers",
                        "duration": "173493"
                    },
                    {
                        "number": "10",
                        "title": "High Fidelity",
                        "duration": "362506"
                    },
                    {
                        "number": "11",
                        "title": "Rock'n Roll",
                        "duration": "453826"
                    },
                    {
                        "number": "12",
                        "title": "Oh Yeah",
                        "duration": "121200"
                    },
                    {
                        "number": "13",
                        "title": "Burnin'",
                        "duration": "413666"
                    },
                    {
                        "number": "14",
                        "title": "Indo Silver Club",
                        "duration": "274733"
                    },
                    {
                        "number": "15",
                        "title": "Alive",
                        "duration": "315266"
                    },
                    {
                        "number": "16",
                        "title": "Funk Ad",
                        "duration": "51240"
                    }
                ]
            },
            {
                "id": "2112975",
                "title": "Human After All",
                "year": "2005",
                "genre": "House",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Human After All",
                        "duration": "319226"
                    },
                    {
                        "number": "2",
                        "title": "The Prime Time of Your Life",
                        "duration": "263373"
                    },
                    {
                        "number": "3",
                        "title": "Robot Rock",
                        "duration": "287760"
                    },
                    {
                        "number": "4",
                        "title": "Steam Machine",
                        "duration": "320800"
                    },
                    {
                        "number": "5",
                        "title": "Make Love",
                        "duration": "290000"
                    },
                    {
                        "number": "6",
                        "title": "The Brainwasher",
                        "duration": "248240"
                    },
                    {
                        "number": "7",
                        "title": "On/Off",
                        "duration": "19333"
                    },
                    {
                        "number": "8",
                        "title": "Television Rules the Nation",
                        "duration": "287733"
                    },
                    {
                        "number": "9",
                        "title": "Technologic",
                        "duration": "284360"
                    },
                    {
                        "number": "10",
                        "title": "Emotion",
                        "duration": "418066"
                    }
                ]
            },
            {
                "id": "2118619",
                "title": "TRON: Legacy",
                "year": "2010",
                "genre": "House",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Overture",
                        "duration": "148000"
                    },
                    {
                        "number": "2",
                        "title": "The Grid",
                        "duration": "96000"
                    },
                    {
                        "number": "3",
                        "title": "The Son of Flynn",
                        "duration": "95000"
                    },
                    {
                        "number": "4",
                        "title": "Recognizer",
                        "duration": "157000"
                    },
                    {
                        "number": "5",
                        "title": "Armory",
                        "duration": "122000"
                    },
                    {
                        "number": "6",
                        "title": "Arena",
                        "duration": "93000"
                    },
                    {
                        "number": "7",
                        "title": "Rinzler",
                        "duration": "137000"
                    },
                    {
                        "number": "8",
                        "title": "The Game Has Changed",
                        "duration": "205000"
                    },
                    {
                        "number": "9",
                        "title": "Outlands",
                        "duration": "162000"
                    },
                    {
                        "number": "10",
                        "title": "Adagio for TRON",
                        "duration": "251000"
                    },
                    {
                        "number": "11",
                        "title": "Nocturne",
                        "duration": "101000"
                    },
                    {
                        "number": "12",
                        "title": "End of Line",
                        "duration": "156000"
                    },
                    {
                        "number": "13",
                        "title": "Derezzed",
                        "duration": "104000"
                    },
                    {
                        "number": "14",
                        "title": "Fall",
                        "duration": "82000"
                    },
                    {
                        "number": "15",
                        "title": "Solar Sailer",
                        "duration": "162000"
                    },
                    {
                        "number": "16",
                        "title": "Rectifier",
                        "duration": "134000"
                    },
                    {
                        "number": "17",
                        "title": "Disc Wars",
                        "duration": "251000"
                    },
                    {
                        "number": "18",
                        "title": "C.L.U.",
                        "duration": "279000"
                    },
                    {
                        "number": "19",
                        "title": "Arrival",
                        "duration": "120000"
                    },
                    {
                        "number": "20",
                        "title": "Flynn Lives",
                        "duration": "202000"
                    },
                    {
                        "number": "21",
                        "title": "TRON Legacy (End Titles)",
                        "duration": "197000"
                    },
                    {
                        "number": "22",
                        "title": "Finale",
                        "duration": "262000"
                    },
                    {
                        "number": "23",
                        "title": "Father and Son",
                        "duration": "189000"
                    },
                    {
                        "number": "24",
                        "title": "Outlands, Part II",
                        "duration": "173000"
                    }
                ]
            },
            {
                "id": "2118620",
                "title": "TRON: Legacy R3CONF1GUR3D",
                "year": "2011",
                "genre": "House",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Derezzed (The Glitch Mob remix)",
                        "duration": "262000"
                    },
                    {
                        "number": "2",
                        "title": "Fall (M83 vs. Big Black Delta remix)",
                        "duration": "235000"
                    },
                    {
                        "number": "3",
                        "title": "The Grid (The Crystal Method remix)",
                        "duration": "268000"
                    },
                    {
                        "number": "4",
                        "title": "Adagio for TRON (Teddybears remix)",
                        "duration": "334000"
                    },
                    {
                        "number": "5",
                        "title": "The Son of Flynn (Ki:Theory remix)",
                        "duration": "291000"
                    },
                    {
                        "number": "6",
                        "title": "C.L.U. (Paul Oakenfold remix)",
                        "duration": "275000"
                    },
                    {
                        "number": "7",
                        "title": "The Son of Flynn (Moby remix)",
                        "duration": "392000"
                    },
                    {
                        "number": "8",
                        "title": "End of Line (Boys Noize remix)",
                        "duration": "340000"
                    },
                    {
                        "number": "9",
                        "title": "Rinzler (Kaskade remix)",
                        "duration": "412000"
                    },
                    {
                        "number": "10",
                        "title": "Encom, Part II (Com Truise remix)",
                        "duration": "292000"
                    },
                    {
                        "number": "11",
                        "title": "End of Line (Photek remix)",
                        "duration": "319000"
                    },
                    {
                        "number": "12",
                        "title": "Arena (The Japanese Popstars remix)",
                        "duration": "368000"
                    },
                    {
                        "number": "13",
                        "title": "Derezzed (Avicii remix)",
                        "duration": "304000"
                    },
                    {
                        "number": "14",
                        "title": "Solar Sailer (Pretty Lights remix)",
                        "duration": "273000"
                    },
                    {
                        "number": "15",
                        "title": "TRON: Legacy (End Titles) (Sander Kleinenberg remix)",
                        "duration": "304000"
                    }
                ]
            },
            {
                "id": "2118654",
                "title": "Discovery",
                "year": "2001",
                "genre": "House",
                "tracks": [
                    {
                        "number": "1",
                        "title": "One More Time",
                        "duration": "320840"
                    },
                    {
                        "number": "2",
                        "title": "Aerodynamic",
                        "duration": "207533"
                    },
                    {
                        "number": "3",
                        "title": "Digital Love",
                        "duration": "298333"
                    },
                    {
                        "number": "4",
                        "title": "Harder, Better, Faster, Stronger",
                        "duration": "224293"
                    },
                    {
                        "number": "5",
                        "title": "Crescendolls",
                        "duration": "211640"
                    },
                    {
                        "number": "6",
                        "title": "Nightvision",
                        "duration": "104466"
                    },
                    {
                        "number": "7",
                        "title": "Superheroes",
                        "duration": "237800"
                    },
                    {
                        "number": "8",
                        "title": "High Life",
                        "duration": "201800"
                    },
                    {
                        "number": "9",
                        "title": "Something About Us",
                        "duration": "231066"
                    },
                    {
                        "number": "10",
                        "title": "Voyager",
                        "duration": "227866"
                    },
                    {
                        "number": "11",
                        "title": "Veridis Quo",
                        "duration": "344893"
                    },
                    {
                        "number": "12",
                        "title": "Short Circuit",
                        "duration": "206866"
                    },
                    {
                        "number": "13",
                        "title": "Face to Face",
                        "duration": "240173"
                    },
                    {
                        "number": "14",
                        "title": "Too Long",
                        "duration": "600293"
                    }
                ]
            },
            {
                "id": "2120081",
                "title": "Alive 2007",
                "year": "2007",
                "genre": "House",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Robot Rock / Oh Yeah",
                        "duration": "387506"
                    },
                    {
                        "number": "2",
                        "title": "Touch It / Technologic",
                        "duration": "329653"
                    },
                    {
                        "number": "3",
                        "title": "Television Rules the Nation / Crescendolls",
                        "duration": "290840"
                    },
                    {
                        "number": "4",
                        "title": "Too Long / Steam Machine",
                        "duration": "421600"
                    },
                    {
                        "number": "5",
                        "title": "Around the World / Harder, Better, Faster, Stronger",
                        "duration": "342626"
                    },
                    {
                        "number": "6",
                        "title": "Burnin' / Too Long",
                        "duration": "431506"
                    },
                    {
                        "number": "7",
                        "title": "Face to Face / Short Circuit",
                        "duration": "295226"
                    },
                    {
                        "number": "8",
                        "title": "One More Time / Aerodynamic",
                        "duration": "370533"
                    },
                    {
                        "number": "9",
                        "title": "Aerodynamic Beats / Gabrielle - Forget About the World (Daft Punk remix)",
                        "duration": "211760"
                    },
                    {
                        "number": "10",
                        "title": "The Prime Time of Your Life / The Brainwasher / Rollin' and Scratchin' / Alive",
                        "duration": "622480"
                    },
                    {
                        "number": "11",
                        "title": "Da Funk / Daftendirekt",
                        "duration": "396973"
                    },
                    {
                        "number": "12",
                        "title": "Superheroes / Human After All / Rock'n Roll",
                        "duration": "341106"
                    },
                    {
                        "number": "1",
                        "title": "Human After All / Together / One More Time (reprise) / Stardust \u00e2\u20ac\u201c Music Sounds Better With You",
                        "duration": "598666"
                    }
                ]
            },
            {
                "id": "2120091",
                "title": "Musique, Volume 1: 1993-2005",
                "year": "2006",
                "genre": "House",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Da Funk",
                        "duration": "323000"
                    },
                    {
                        "number": "2",
                        "title": "Around the World",
                        "duration": "240000"
                    },
                    {
                        "number": "3",
                        "title": "Burnin'",
                        "duration": "225000"
                    },
                    {
                        "number": "4",
                        "title": "Revolution 909",
                        "duration": "234000"
                    },
                    {
                        "number": "5",
                        "title": "One More Time",
                        "duration": "225000"
                    },
                    {
                        "number": "6",
                        "title": "Harder, Better, Faster, Stronger",
                        "duration": "222000"
                    },
                    {
                        "number": "7",
                        "title": "Something About Us",
                        "duration": "132000"
                    },
                    {
                        "number": "8",
                        "title": "Robot Rock",
                        "duration": "193000"
                    },
                    {
                        "number": "9",
                        "title": "Technologic",
                        "duration": "174000"
                    },
                    {
                        "number": "10",
                        "title": "Rollin' & Scratchin' (live in L.A.)",
                        "duration": "518000"
                    },
                    {
                        "number": "11",
                        "title": "The Prime Time of Your Life",
                        "duration": "243000"
                    },
                    {
                        "number": "12",
                        "title": "Robot Rock (Maximum Overdrive)",
                        "duration": "358000"
                    }
                ]
            },
            {
                "id": "2162908",
                "title": "Random Access Memories",
                "year": "2013",
                "genre": "House",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Give Life Back to Music",
                        "duration": "274000"
                    },
                    {
                        "number": "2",
                        "title": "The Game of Love",
                        "duration": "321000"
                    },
                    {
                        "number": "3",
                        "title": "Giorgio by Moroder",
                        "duration": "544000"
                    },
                    {
                        "number": "4",
                        "title": "Within",
                        "duration": "228000"
                    },
                    {
                        "number": "5",
                        "title": "Instant Crush",
                        "duration": "337000"
                    },
                    {
                        "number": "6",
                        "title": "Lose Yourself to Dance",
                        "duration": "353000"
                    },
                    {
                        "number": "7",
                        "title": "Touch",
                        "duration": "498000"
                    },
                    {
                        "number": "8",
                        "title": "Get Lucky",
                        "duration": "367000"
                    },
                    {
                        "number": "9",
                        "title": "Beyond",
                        "duration": "290000"
                    },
                    {
                        "number": "10",
                        "title": "Motherboard",
                        "duration": "341000"
                    },
                    {
                        "number": "11",
                        "title": "Fragments of Time",
                        "duration": "279000"
                    },
                    {
                        "number": "12",
                        "title": "Doin' It Right",
                        "duration": "251000"
                    },
                    {
                        "number": "13",
                        "title": "Contact",
                        "duration": "381000"
                    },
                    {
                        "number": "14",
                        "title": "Horizon",
                        "duration": "264000"
                    }
                ]
            },
            {
                "id": "2197190",
                "title": "Daft Club",
                "year": "2003",
                "genre": "House",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Ouverture",
                        "duration": "161000"
                    },
                    {
                        "number": "2",
                        "title": "Aerodynamic (Daft Punk remix)",
                        "duration": "371000"
                    },
                    {
                        "number": "3",
                        "title": "Harder, Better, Faster, Stronger (The Neptunes remix)",
                        "duration": "311000"
                    },
                    {
                        "number": "4",
                        "title": "Face to Face (Cosmo Vitelli remix)",
                        "duration": "295000"
                    },
                    {
                        "number": "5",
                        "title": "Phoenix (Basement Jaxx remix)",
                        "duration": "473000"
                    },
                    {
                        "number": "6",
                        "title": "Digital Love (Boris Dlugosch remix)",
                        "duration": "451000"
                    },
                    {
                        "number": "7",
                        "title": "Harder, Better, Faster, Stronger (Jess and Crabbe Regulator mix)",
                        "duration": "361000"
                    },
                    {
                        "number": "8",
                        "title": "Face to Face (Demon remix)",
                        "duration": "420000"
                    },
                    {
                        "number": "9",
                        "title": "Crescendolls (Laidback Luke remix)",
                        "duration": "326000"
                    },
                    {
                        "number": "10",
                        "title": "Aerodynamic (Slum Village remix)",
                        "duration": "218000"
                    },
                    {
                        "number": "11",
                        "title": "Too Long (Gonzales version)",
                        "duration": "194000"
                    },
                    {
                        "number": "12",
                        "title": "Aerodynamite",
                        "duration": "468000"
                    },
                    {
                        "number": "13",
                        "title": "One More Time (Romanthony's unplugged)",
                        "duration": "221000"
                    },
                    {
                        "number": "14",
                        "title": "Something About Us (Love Theme From Interstella 5555)",
                        "duration": "134000"
                    }
                ]
            },
            {
                "id": "2197191",
                "title": "Alive 1997",
                "year": "2001",
                "genre": "House",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Alive 1997",
                        "duration": "2731000"
                    }
                ]
            },
            {
                "id": "2197192",
                "title": "Human After All: Remixes",
                "year": "2006",
                "genre": "House",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Robot Rock (Soulwax remix)",
                        "duration": "391000"
                    },
                    {
                        "number": "2",
                        "title": "Human After All (SebastiAn remix)",
                        "duration": "287000"
                    },
                    {
                        "number": "3",
                        "title": "Technologic (Peaches No Logic remix)",
                        "duration": "277000"
                    },
                    {
                        "number": "4",
                        "title": "Brainwasher (Erol Alkan's Horrorhouse dub)",
                        "duration": "365000"
                    },
                    {
                        "number": "5",
                        "title": "Prime Time of Your Life (Para One remix)",
                        "duration": "231000"
                    },
                    {
                        "number": "6",
                        "title": "Human After All (\"Guy-Man After All\" Justice remix)",
                        "duration": "240000"
                    },
                    {
                        "number": "7",
                        "title": "Technologic (Digitalism's Highway to Paris remix)",
                        "duration": "361000"
                    },
                    {
                        "number": "8",
                        "title": "Human After All (Alter Ego remix)",
                        "duration": "565000"
                    },
                    {
                        "number": "9",
                        "title": "Technologic (Vitalic remix)",
                        "duration": "326000"
                    },
                    {
                        "number": "10",
                        "title": "Robot Rock (Maximum Overdrive)",
                        "duration": "354000"
                    }
                ]
            },
            {
                "id": "2246842",
                "title": "Da Funk",
                "year": "1995",
                "genre": "House",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Da Funk",
                        "duration": "333493"
                    },
                    {
                        "number": "2",
                        "title": "Musique",
                        "duration": "411507"
                    }
                ]
            },
            {
                "id": "2267389",
                "title": "2006-04-29: Coachella Valley Music Festival",
                "year": "2006",
                "genre": "House",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Robot Rock",
                        "duration": "390000"
                    },
                    {
                        "number": "2",
                        "title": "Technologic",
                        "duration": "329000"
                    },
                    {
                        "number": "3",
                        "title": "Television Rules the Nation",
                        "duration": "290000"
                    },
                    {
                        "number": "4",
                        "title": "Steam Machine",
                        "duration": "436000"
                    },
                    {
                        "number": "5",
                        "title": "Around the World (Harder, Better, Faster, Stronger)",
                        "duration": "448000"
                    },
                    {
                        "number": "6",
                        "title": "Too Long",
                        "duration": "298000"
                    },
                    {
                        "number": "7",
                        "title": "Face to Face (Harder remix)",
                        "duration": "222000"
                    },
                    {
                        "number": "8",
                        "title": "Interlude",
                        "duration": "100000"
                    },
                    {
                        "number": "9",
                        "title": "One More Time (Aerodynamic remix)",
                        "duration": "522000"
                    },
                    {
                        "number": "10",
                        "title": "The Brainwashers (Rollin' & Scratchin' remix)",
                        "duration": "454000"
                    },
                    {
                        "number": "11",
                        "title": "Alive (The Prime Time of Your Life remix)",
                        "duration": "198000"
                    },
                    {
                        "number": "12",
                        "title": "Da Funk",
                        "duration": "398000"
                    },
                    {
                        "number": "13",
                        "title": "Human After All (Superheroes remix)",
                        "duration": "432000"
                    }
                ]
            },
            {
                "id": "2342066",
                "title": "TRON Legacy: For Your Consideration Academy Promo",
                "year": "2010",
                "genre": '',
                "tracks": [
                    {
                        "number": "1",
                        "title": "Legacy Open",
                        "duration": "96000"
                    },
                    {
                        "number": "2",
                        "title": "Motochase",
                        "duration": "95000"
                    },
                    {
                        "number": "3",
                        "title": "Recognizer Capture",
                        "duration": "157000"
                    },
                    {
                        "number": "4",
                        "title": "Sirens",
                        "duration": "123000"
                    },
                    {
                        "number": "5",
                        "title": "Disc Game (intro)",
                        "duration": "93000"
                    },
                    {
                        "number": "6",
                        "title": "Rinzler Vs. Sam",
                        "duration": "137000"
                    },
                    {
                        "number": "7",
                        "title": "Lightbikes Battle",
                        "duration": "205000"
                    },
                    {
                        "number": "8",
                        "title": "Qudrra Saves Same",
                        "duration": "162000"
                    },
                    {
                        "number": "9",
                        "title": "Flynn's Flashback",
                        "duration": "251000"
                    },
                    {
                        "number": "10",
                        "title": "Sam Plans Escape",
                        "duration": "101000"
                    },
                    {
                        "number": "11",
                        "title": "End of Line",
                        "duration": "156000"
                    },
                    {
                        "number": "12",
                        "title": "Party Crashers",
                        "duration": "104000"
                    },
                    {
                        "number": "13",
                        "title": "Flynn Drops In",
                        "duration": "82000"
                    },
                    {
                        "number": "14",
                        "title": "Solar Sailer Alt.",
                        "duration": "162000"
                    },
                    {
                        "number": "15",
                        "title": "Clu Speech",
                        "duration": "134000"
                    },
                    {
                        "number": "16",
                        "title": "Recovering the Disc",
                        "duration": "251000"
                    },
                    {
                        "number": "17",
                        "title": "Lightjets",
                        "duration": "279000"
                    },
                    {
                        "number": "18",
                        "title": "Portal Arrival",
                        "duration": "120000"
                    },
                    {
                        "number": "19",
                        "title": "Portal Climax",
                        "duration": "212000"
                    },
                    {
                        "number": "20",
                        "title": "Legacy Theme",
                        "duration": "197000"
                    }
                ]
            },
            {
                "id": "2360114",
                "title": "The New Wave",
                "year": "1994",
                "genre": '',
                "tracks": [
                    {
                        "number": "1",
                        "title": "The New Wave (edit)",
                        "duration": "317000"
                    },
                    {
                        "number": "2",
                        "title": "The New Wave (full length)",
                        "duration": "432000"
                    },
                    {
                        "number": "3",
                        "title": "Assault",
                        "duration": "346000"
                    },
                    {
                        "number": "4",
                        "title": "Alive",
                        "duration": "315000"
                    }
                ]
            }
        ]
    },
    "The Prodigy": {
        "albums": [
            {
                "id": "2116421",
                "title": "Always Outnumbered, Never Outgunned",
                "year": "2004",
                "genre": "Big Beat",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Spitfire",
                        "duration": "307786"
                    },
                    {
                        "number": "2",
                        "title": "Girls",
                        "duration": "247200"
                    },
                    {
                        "number": "3",
                        "title": "Memphis Bells",
                        "duration": "268826"
                    },
                    {
                        "number": "4",
                        "title": "Get Up Get Off",
                        "duration": "259586"
                    },
                    {
                        "number": "5",
                        "title": "Hot Ride",
                        "duration": "276226"
                    },
                    {
                        "number": "6",
                        "title": "Wake Up Call",
                        "duration": "296373"
                    },
                    {
                        "number": "7",
                        "title": "Action Radar",
                        "duration": "332746"
                    },
                    {
                        "number": "8",
                        "title": "Medusa's Path",
                        "duration": "368826"
                    },
                    {
                        "number": "9",
                        "title": "Phoenix",
                        "duration": "278866"
                    },
                    {
                        "number": "10",
                        "title": "You'll Be Under My Wheels",
                        "duration": "236973"
                    },
                    {
                        "number": "11",
                        "title": "The Way It Is",
                        "duration": "346413"
                    },
                    {
                        "number": "12",
                        "title": "Shoot Down",
                        "duration": "268174"
                    }
                ]
            },
            {
                "id": "2116422",
                "title": "Experience",
                "year": "1992",
                "genre": "Big Beat",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Jericho",
                        "duration": "223866"
                    },
                    {
                        "number": "2",
                        "title": "Music Reach (1/2/3/4)",
                        "duration": "252093"
                    },
                    {
                        "number": "3",
                        "title": "Wind It Up",
                        "duration": "273066"
                    },
                    {
                        "number": "4",
                        "title": "Your Love (remix)",
                        "duration": "331266"
                    },
                    {
                        "number": "5",
                        "title": "Hyperspeed (G-Force, Part 2)",
                        "duration": "315066"
                    },
                    {
                        "number": "6",
                        "title": "Charly (Trip Into Drum and Bass version)",
                        "duration": "312706"
                    },
                    {
                        "number": "7",
                        "title": "Out of Space",
                        "duration": "298226"
                    },
                    {
                        "number": "8",
                        "title": "Everybody in the Place (155 and Rising)",
                        "duration": "250973"
                    },
                    {
                        "number": "9",
                        "title": "Weather Experience",
                        "duration": "484826"
                    },
                    {
                        "number": "10",
                        "title": "Fire (Sunrise version)",
                        "duration": "297933"
                    },
                    {
                        "number": "11",
                        "title": "Ruff in the Jungle Bizness",
                        "duration": "310266"
                    },
                    {
                        "number": "12",
                        "title": "Death of the Prodigy Dancers",
                        "duration": "223066"
                    }
                ]
            },
            {
                "id": "2116423",
                "title": "The Fat of the Land",
                "year": "1997",
                "genre": "Big Beat",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Smack My Bitch Up",
                        "duration": "342733"
                    },
                    {
                        "number": "2",
                        "title": "Breathe",
                        "duration": "334800"
                    },
                    {
                        "number": "3",
                        "title": "Diesel Power",
                        "duration": "257600"
                    },
                    {
                        "number": "4",
                        "title": "Funky Shit",
                        "duration": "316426"
                    },
                    {
                        "number": "5",
                        "title": "Serial Thrilla",
                        "duration": "311333"
                    },
                    {
                        "number": "6",
                        "title": "Mindfields",
                        "duration": "339906"
                    },
                    {
                        "number": "7",
                        "title": "Narayan",
                        "duration": "545960"
                    },
                    {
                        "number": "8",
                        "title": "Firestarter",
                        "duration": "281240"
                    },
                    {
                        "number": "9",
                        "title": "Climbatize",
                        "duration": "396893"
                    },
                    {
                        "number": "10",
                        "title": "Fuel My Fire",
                        "duration": "258906"
                    }
                ]
            },
            {
                "id": "2116424",
                "title": "Invaders Must Die",
                "year": "2009",
                "genre": "Big Beat",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Invaders Must Die",
                        "duration": "295000"
                    },
                    {
                        "number": "2",
                        "title": "Omen",
                        "duration": "216000"
                    },
                    {
                        "number": "3",
                        "title": "Thunder",
                        "duration": "249000"
                    },
                    {
                        "number": "4",
                        "title": "Colours",
                        "duration": "207000"
                    },
                    {
                        "number": "5",
                        "title": "Take Me to the Hospital",
                        "duration": "220000"
                    },
                    {
                        "number": "6",
                        "title": "Warrior's Dance",
                        "duration": "312000"
                    },
                    {
                        "number": "7",
                        "title": "Run With the Wolves",
                        "duration": "264000"
                    },
                    {
                        "number": "8",
                        "title": "Omen (reprise)",
                        "duration": "134000"
                    },
                    {
                        "number": "9",
                        "title": "World's on Fire",
                        "duration": "290000"
                    },
                    {
                        "number": "10",
                        "title": "Piranha",
                        "duration": "244000"
                    },
                    {
                        "number": "11",
                        "title": "Stand Up",
                        "duration": "330000"
                    }
                ]
            },
            {
                "id": "2116425",
                "title": "Music for the Jilted Generation",
                "year": "1994",
                "genre": "Big Beat",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Intro",
                        "duration": "46266"
                    },
                    {
                        "number": "2",
                        "title": "Break & Enter",
                        "duration": "504426"
                    },
                    {
                        "number": "3",
                        "title": "Their Law (feat. Pop Will Eat Itself)",
                        "duration": "400773"
                    },
                    {
                        "number": "4",
                        "title": "Full Throttle",
                        "duration": "302560"
                    },
                    {
                        "number": "5",
                        "title": "Voodoo People",
                        "duration": "387000"
                    },
                    {
                        "number": "6",
                        "title": "Speedway (Theme From Fastlane)",
                        "duration": "536373"
                    },
                    {
                        "number": "7",
                        "title": "The Heat (The Energy)",
                        "duration": "267733"
                    },
                    {
                        "number": "8",
                        "title": "Poison",
                        "duration": "402466"
                    },
                    {
                        "number": "9",
                        "title": "No Good (Start the Dance)",
                        "duration": "377893"
                    },
                    {
                        "number": "10",
                        "title": "One Love (edit)",
                        "duration": "233466"
                    },
                    {
                        "number": "11",
                        "title": "The Narcotic Suite: 3 Kilos",
                        "duration": "445906"
                    },
                    {
                        "number": "12",
                        "title": "The Narcotic Suite: Skylined",
                        "duration": "358093"
                    },
                    {
                        "number": "13",
                        "title": "The Narcotic Suite: Claustrophobic Sting",
                        "duration": "431906"
                    }
                ]
            },
            {
                "id": "2118309",
                "title": "Their Law: The Singles 1990-2005",
                "year": "2005",
                "genre": "Big Beat",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Firestarter",
                        "duration": "282626"
                    },
                    {
                        "number": "2",
                        "title": "Their Law",
                        "duration": "336240"
                    },
                    {
                        "number": "3",
                        "title": "Breathe",
                        "duration": "336280"
                    },
                    {
                        "number": "4",
                        "title": "Out of Space",
                        "duration": "302106"
                    },
                    {
                        "number": "5",
                        "title": "Smack My Bitch Up",
                        "duration": "343386"
                    },
                    {
                        "number": "6",
                        "title": "Poison",
                        "duration": "241200"
                    },
                    {
                        "number": "7",
                        "title": "Girls (feat. The Ping Pong Bitches)",
                        "duration": "252573"
                    },
                    {
                        "number": "8",
                        "title": "Voodoo People",
                        "duration": "220133"
                    },
                    {
                        "number": "9",
                        "title": "Charly (Alley Cat remix)",
                        "duration": "322986"
                    },
                    {
                        "number": "10",
                        "title": "No Good (Start the Dance)",
                        "duration": "379906"
                    },
                    {
                        "number": "11",
                        "title": "Spitfire",
                        "duration": "206880"
                    },
                    {
                        "number": "12",
                        "title": "Jericho",
                        "duration": "226933"
                    },
                    {
                        "number": "13",
                        "title": "Everybody in the Place (Fairground remix)",
                        "duration": "309600"
                    },
                    {
                        "number": "14",
                        "title": "One Love",
                        "duration": "325133"
                    },
                    {
                        "number": "15",
                        "title": "Hot Ride",
                        "duration": "272920"
                    },
                    {
                        "number": "1",
                        "title": "Razor",
                        "duration": "240173"
                    },
                    {
                        "number": "2",
                        "title": "Back 2 Skool",
                        "duration": "302280"
                    },
                    {
                        "number": "3",
                        "title": "Voodoo People (Pendulum remix)",
                        "duration": "307813"
                    },
                    {
                        "number": "4",
                        "title": "Under My Wheels (remix)",
                        "duration": "194826"
                    },
                    {
                        "number": "5",
                        "title": "No Man Army",
                        "duration": "250480"
                    },
                    {
                        "number": "6",
                        "title": "Molotov Bitch",
                        "duration": "294493"
                    },
                    {
                        "number": "7",
                        "title": "Voodoo Beats",
                        "duration": "234360"
                    },
                    {
                        "number": "8",
                        "title": "Out of Space (Audio Bullys remix)",
                        "duration": "296680"
                    },
                    {
                        "number": "9",
                        "title": "The Way It Is (live remix)",
                        "duration": "256866"
                    },
                    {
                        "number": "10",
                        "title": "We Are the Ruffest",
                        "duration": "318813"
                    },
                    {
                        "number": "11",
                        "title": "Your Love",
                        "duration": "362666"
                    },
                    {
                        "number": "12",
                        "title": "Spitfire (live)",
                        "duration": "251666"
                    },
                    {
                        "number": "13",
                        "title": "Their Law (live)",
                        "duration": "331813"
                    },
                    {
                        "number": "14",
                        "title": "Breathe (live)",
                        "duration": "399866"
                    },
                    {
                        "number": "15",
                        "title": "Serial Thrilla (live)",
                        "duration": "315493"
                    },
                    {
                        "number": "16",
                        "title": "Firestarter (live)",
                        "duration": "321280"
                    }
                ]
            },
            {
                "id": "2127250",
                "title": "Remixers Must Die",
                "year": "2009",
                "genre": "Big Beat",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Invaders Must Die (Aquila Killed the Carebears mix)",
                        "duration": "210000"
                    },
                    {
                        "number": "2",
                        "title": "Omen (Aquila remix)",
                        "duration": "302000"
                    },
                    {
                        "number": "3",
                        "title": "Thunder (Moozeblaster remix)",
                        "duration": "283000"
                    },
                    {
                        "number": "4",
                        "title": "Colours (Darkwave remix)",
                        "duration": "281000"
                    },
                    {
                        "number": "5",
                        "title": "Take Me to the Hospital (Deliverusfromevil's Dementia mix)",
                        "duration": "215000"
                    },
                    {
                        "number": "6",
                        "title": "Warriors Dance (N2rmx)",
                        "duration": "245000"
                    },
                    {
                        "number": "7",
                        "title": "Run With the Wolves (Lothario remix)",
                        "duration": "245000"
                    },
                    {
                        "number": "8",
                        "title": "Omen Reprise (Denu remix)",
                        "duration": "316000"
                    },
                    {
                        "number": "9",
                        "title": "World's on Fire (Memphis remix)",
                        "duration": "352000"
                    },
                    {
                        "number": "10",
                        "title": "Piranha (Baltars Dream Piranha reprise mix)",
                        "duration": "162000"
                    },
                    {
                        "number": "11",
                        "title": "Stand Up (Chelarazor mix)",
                        "duration": "236000"
                    },
                    {
                        "number": "12",
                        "title": "The Big Gundown (Baltars Dream remix)",
                        "duration": "256000"
                    },
                    {
                        "number": "13",
                        "title": "Wild West (Catlaunch3r remix)",
                        "duration": "214000"
                    },
                    {
                        "number": "14",
                        "title": "Black Smoke (90s Break the House remix)",
                        "duration": "328000"
                    },
                    {
                        "number": "15",
                        "title": "Fighter Beat (N2rmx)",
                        "duration": "231000"
                    }
                ]
            },
            {
                "id": "2180096",
                "title": "Baby's Got a Temper",
                "year": "2002",
                "genre": "Big Beat",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Baby's Got a Temper (original version)",
                        "duration": "268800"
                    },
                    {
                        "number": "2",
                        "title": "Baby's Got a Temper (dub)",
                        "duration": "359666"
                    }
                ]
            },
            {
                "id": "2206416",
                "title": "Always Outsiders, Never Outdone: Prodigy Remixed",
                "year": "2004",
                "genre": "Big Beat",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Spitfire (FakeIDs Evolution)",
                        "duration": "392773"
                    },
                    {
                        "number": "2",
                        "title": "Girls (idiotech remix)",
                        "duration": "312680"
                    },
                    {
                        "number": "3",
                        "title": "Jungle Bells (Dunproofin mix)",
                        "duration": "271093"
                    },
                    {
                        "number": "4",
                        "title": "Get Up Get Off (Fujikato+Dancingdiscoduke remix)",
                        "duration": "260906"
                    },
                    {
                        "number": "5",
                        "title": "Hotride (Poj mix)",
                        "duration": "194426"
                    },
                    {
                        "number": "6",
                        "title": "Been Up Long (Falsedawn)",
                        "duration": "268920"
                    },
                    {
                        "number": "7",
                        "title": "Action Radar (FakeID mix)",
                        "duration": "462386"
                    },
                    {
                        "number": "8",
                        "title": "Medusa Bitch (cry.on.my.console)",
                        "duration": "157413"
                    },
                    {
                        "number": "9",
                        "title": "Phoenus (Pop Razors)",
                        "duration": "305893"
                    },
                    {
                        "number": "10",
                        "title": "You Will Be Under My Satanic Wheels (Act of Dog)",
                        "duration": "319360"
                    },
                    {
                        "number": "11",
                        "title": "The Way It Is (Elektric Cowboy)",
                        "duration": "346400"
                    },
                    {
                        "number": "12",
                        "title": "Shoot Down (Fujikato remix)",
                        "duration": "219000"
                    }
                ]
            },
            {
                "id": "2231648",
                "title": "The Day Is My Enemy",
                "year": "2015",
                "genre": "Big Beat",
                "tracks": [
                    {
                        "number": "1",
                        "title": "The Day Is My Enemy",
                        "duration": "264947"
                    },
                    {
                        "number": "2",
                        "title": "Nasty",
                        "duration": "243467"
                    },
                    {
                        "number": "3",
                        "title": "Rebel Radio",
                        "duration": "232214"
                    },
                    {
                        "number": "4",
                        "title": "Ibiza",
                        "duration": "165614"
                    },
                    {
                        "number": "5",
                        "title": "Destroy",
                        "duration": "268534"
                    },
                    {
                        "number": "6",
                        "title": "Wild Frontier",
                        "duration": "268000"
                    },
                    {
                        "number": "7",
                        "title": "Rok-Weiler",
                        "duration": "230680"
                    },
                    {
                        "number": "8",
                        "title": "Beyond the Deathray",
                        "duration": "188827"
                    },
                    {
                        "number": "9",
                        "title": "Rhythm Bomb",
                        "duration": "252320"
                    },
                    {
                        "number": "10",
                        "title": "Roadblox",
                        "duration": "300894"
                    },
                    {
                        "number": "11",
                        "title": "Get Your Fight On",
                        "duration": "218774"
                    },
                    {
                        "number": "12",
                        "title": "Medicine",
                        "duration": "236014"
                    },
                    {
                        "number": "13",
                        "title": "Invisible Sun",
                        "duration": "256040"
                    },
                    {
                        "number": "14",
                        "title": "Wall of Death",
                        "duration": "252187"
                    },
                    {
                        "number": "15",
                        "title": "Rise of the Eagles",
                        "duration": "227576"
                    }
                ]
            },
            {
                "id": "2262671",
                "title": "No Good (Start the Dance)",
                "year": "1994",
                "genre": "Big Beat",
                "tracks": [
                    {
                        "number": "1",
                        "title": "No Good (Start the Dance) (radio edit)",
                        "duration": "240933"
                    },
                    {
                        "number": "2",
                        "title": "No Good (Start the Dance) (CJ Bolland's Museum mix)",
                        "duration": "315533"
                    },
                    {
                        "number": "3",
                        "title": "One Love (Jonny L remix)",
                        "duration": "305360"
                    },
                    {
                        "number": "4",
                        "title": "Jericho (Genaside II remix)",
                        "duration": "337706"
                    },
                    {
                        "number": "5",
                        "title": "G-Force (Energy Flow)",
                        "duration": "323293"
                    }
                ]
            },
            {
                "id": "2262672",
                "title": "Out of Space (The Very Best)",
                "year": "0",
                "genre": "Big Beat",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Smack My Bitch Up",
                        "duration": "288253"
                    },
                    {
                        "number": "2",
                        "title": "Breathe",
                        "duration": "336453"
                    },
                    {
                        "number": "3",
                        "title": "No Good (Start the Dance) (original mix)",
                        "duration": "378986"
                    },
                    {
                        "number": "4",
                        "title": "Out of Space",
                        "duration": "300320"
                    },
                    {
                        "number": "5",
                        "title": "Firestarter",
                        "duration": "227466"
                    },
                    {
                        "number": "6",
                        "title": "Poison",
                        "duration": "403320"
                    },
                    {
                        "number": "7",
                        "title": "Everybody in the Place",
                        "duration": "252786"
                    },
                    {
                        "number": "8",
                        "title": "Diesel Power",
                        "duration": "258626"
                    },
                    {
                        "number": "9",
                        "title": "Voodoo People",
                        "duration": "326093"
                    },
                    {
                        "number": "10",
                        "title": "Jericho",
                        "duration": "224986"
                    },
                    {
                        "number": "11",
                        "title": "Mindfields",
                        "duration": "340933"
                    },
                    {
                        "number": "12",
                        "title": "One Love",
                        "duration": "233733"
                    },
                    {
                        "number": "13",
                        "title": "Ruff in the Jungle Bizness",
                        "duration": "309960"
                    },
                    {
                        "number": "14",
                        "title": "Funky Shit",
                        "duration": "318480"
                    },
                    {
                        "number": "15",
                        "title": "One Man Army",
                        "duration": "254813"
                    }
                ]
            },
            {
                "id": "2288709",
                "title": "Someself One",
                "year": "1998",
                "genre": "Electronic",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Break & Enter (live)",
                        "duration": "0"
                    },
                    {
                        "number": "2",
                        "title": "Android",
                        "duration": "0"
                    },
                    {
                        "number": "3",
                        "title": "Diesel Power",
                        "duration": "0"
                    },
                    {
                        "number": "4",
                        "title": "Retribution '93",
                        "duration": "0"
                    },
                    {
                        "number": "5",
                        "title": "Release Yo'Delf (Prodigy mix)",
                        "duration": "0"
                    },
                    {
                        "number": "6",
                        "title": "Everybody in the Place (Fairground remix)",
                        "duration": "0"
                    },
                    {
                        "number": "7",
                        "title": "Rip Up the Sound System",
                        "duration": "0"
                    },
                    {
                        "number": "8",
                        "title": "One Man Army",
                        "duration": "0"
                    },
                    {
                        "number": "9",
                        "title": "Zeroes & Ones (The Prodigy vs Jesus Jones mix)",
                        "duration": "0"
                    },
                    {
                        "number": "10",
                        "title": "Casanova (Prodigy Pump Action remix)",
                        "duration": "297000"
                    },
                    {
                        "number": "11",
                        "title": "Rat Poison",
                        "duration": "0"
                    },
                    {
                        "number": "12",
                        "title": "Smack My Bitch Up",
                        "duration": "0"
                    },
                    {
                        "number": "13",
                        "title": "Everybody Say Love (The Prodigy remix)",
                        "duration": "0"
                    },
                    {
                        "number": "14",
                        "title": "No Good (Start the Dance) (Bad for You mix)",
                        "duration": "0"
                    },
                    {
                        "number": "15",
                        "title": "Mindfields",
                        "duration": "0"
                    },
                    {
                        "number": "16",
                        "title": "What Evil Lurks",
                        "duration": "0"
                    },
                    {
                        "number": "17",
                        "title": "Scienide",
                        "duration": "0"
                    }
                ]
            },
            {
                "id": "2308577",
                "title": "No Tourists",
                "year": "2018",
                "genre": "Electronic",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Need Some1",
                        "duration": "165000"
                    },
                    {
                        "number": "2",
                        "title": "Light Up the Sky",
                        "duration": "199000"
                    },
                    {
                        "number": "3",
                        "title": "We Live Forever",
                        "duration": "223000"
                    },
                    {
                        "number": "4",
                        "title": "No Tourists",
                        "duration": "258000"
                    },
                    {
                        "number": "5",
                        "title": "Fight Fire with Fire",
                        "duration": "208000"
                    },
                    {
                        "number": "6",
                        "title": "Timebomb Zone",
                        "duration": "204000"
                    },
                    {
                        "number": "7",
                        "title": "Champions of London",
                        "duration": "289000"
                    },
                    {
                        "number": "8",
                        "title": "Boom Boom Tap",
                        "duration": "245000"
                    },
                    {
                        "number": "9",
                        "title": "Resonate",
                        "duration": "230000"
                    },
                    {
                        "number": "10",
                        "title": "Give Me a Signal",
                        "duration": "241000"
                    }
                ]
            },
            {
                "id": "2313664",
                "title": "Singles Collection",
                "year": "1997",
                "genre": "",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Breathe",
                        "duration": "334920"
                    },
                    {
                        "number": "2",
                        "title": "No Good (Start the Dance) (original mix)",
                        "duration": "377453"
                    },
                    {
                        "number": "3",
                        "title": "Out of Space",
                        "duration": "298786"
                    },
                    {
                        "number": "4",
                        "title": "Firestarter",
                        "duration": "279986"
                    },
                    {
                        "number": "5",
                        "title": "Poison",
                        "duration": "402813"
                    },
                    {
                        "number": "6",
                        "title": "Everybody in the Place",
                        "duration": "251253"
                    },
                    {
                        "number": "7",
                        "title": "Diesel Power",
                        "duration": "258120"
                    },
                    {
                        "number": "8",
                        "title": "Voodoo People",
                        "duration": "386720"
                    },
                    {
                        "number": "9",
                        "title": "Jericho",
                        "duration": "223453"
                    },
                    {
                        "number": "10",
                        "title": "Mindfields",
                        "duration": "340426"
                    },
                    {
                        "number": "11",
                        "title": "One Love",
                        "duration": "233226"
                    },
                    {
                        "number": "12",
                        "title": "Ruff in the Jungle Bizness",
                        "duration": "309453"
                    },
                    {
                        "number": "13",
                        "title": "Funky Shit",
                        "duration": "316946"
                    },
                    {
                        "number": "14",
                        "title": "Charly (Trip Into Drum and Bass version)",
                        "duration": "312760"
                    }
                ]
            },
            {
                "id": "2313665",
                "title": "The Singles",
                "year": "1996",
                "genre": "",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Firestarter (edit)",
                        "duration": "225000"
                    },
                    {
                        "number": "2",
                        "title": "Your Love",
                        "duration": "360000"
                    },
                    {
                        "number": "3",
                        "title": "G-Force (Energy Flow)",
                        "duration": "318000"
                    },
                    {
                        "number": "4",
                        "title": "Fire (Sunrise version)",
                        "duration": "305000"
                    },
                    {
                        "number": "5",
                        "title": "Out of Space (edit)",
                        "duration": "221000"
                    },
                    {
                        "number": "6",
                        "title": "Wind It Up (The Rewound edit)",
                        "duration": "209000"
                    },
                    {
                        "number": "7",
                        "title": "Firestarter (edit)",
                        "duration": "225000"
                    },
                    {
                        "number": "8",
                        "title": "One Love (edit)",
                        "duration": "233000"
                    },
                    {
                        "number": "9",
                        "title": "No Good (Start the Dance) (radio edit)",
                        "duration": "241000"
                    },
                    {
                        "number": "10",
                        "title": "Voodoo People (Dust Brothers remix)",
                        "duration": "356000"
                    },
                    {
                        "number": "11",
                        "title": "Poison (\u201995 edit)",
                        "duration": "241000"
                    },
                    {
                        "number": "12",
                        "title": "Firestarter (edit)",
                        "duration": "225000"
                    }
                ]
            },
            {
                "id": "2313666",
                "title": "Greatest Hits",
                "year": "2009",
                "genre": "",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Omen",
                        "duration": "218000"
                    },
                    {
                        "number": "2",
                        "title": "Girls",
                        "duration": "251000"
                    },
                    {
                        "number": "3",
                        "title": "Worlds on Fire",
                        "duration": "292000"
                    },
                    {
                        "number": "4",
                        "title": "Breathe",
                        "duration": "338000"
                    },
                    {
                        "number": "5",
                        "title": "Voodoo People (Pendulum remix)",
                        "duration": "309000"
                    },
                    {
                        "number": "6",
                        "title": "Take Me to the Hospital",
                        "duration": "222000"
                    },
                    {
                        "number": "7",
                        "title": "Out of Space",
                        "duration": "304000"
                    },
                    {
                        "number": "8",
                        "title": "Smack My Bith Up",
                        "duration": "346000"
                    },
                    {
                        "number": "9",
                        "title": "Spitfire",
                        "duration": "311000"
                    },
                    {
                        "number": "10",
                        "title": "Thunder",
                        "duration": "251000"
                    },
                    {
                        "number": "11",
                        "title": "Firestarter",
                        "duration": "283000"
                    },
                    {
                        "number": "12",
                        "title": "Everybody in the Place",
                        "duration": "311000"
                    },
                    {
                        "number": "13",
                        "title": "You\u2019ll Be Under My Wheels",
                        "duration": "239000"
                    },
                    {
                        "number": "14",
                        "title": "Poison",
                        "duration": "243000"
                    },
                    {
                        "number": "15",
                        "title": "Baby\u2019s Got a Temper",
                        "duration": "269000"
                    },
                    {
                        "number": "16",
                        "title": "Hot Ride",
                        "duration": "280000"
                    },
                    {
                        "number": "17",
                        "title": "Serial Thrilla",
                        "duration": "313000"
                    },
                    {
                        "number": "1",
                        "title": "Invaders Must Die",
                        "duration": "297000"
                    },
                    {
                        "number": "2",
                        "title": "Colours",
                        "duration": "209000"
                    },
                    {
                        "number": "3",
                        "title": "Wake Up Call",
                        "duration": "300000"
                    },
                    {
                        "number": "4",
                        "title": "No Good",
                        "duration": "381000"
                    },
                    {
                        "number": "5",
                        "title": "Diesel Power",
                        "duration": "260000"
                    },
                    {
                        "number": "6",
                        "title": "Their Law",
                        "duration": "338000"
                    },
                    {
                        "number": "7",
                        "title": "Charly",
                        "duration": "324000"
                    },
                    {
                        "number": "8",
                        "title": "One Love",
                        "duration": "327000"
                    },
                    {
                        "number": "9",
                        "title": "Wind It Up",
                        "duration": "276000"
                    },
                    {
                        "number": "10",
                        "title": "Your Love",
                        "duration": "364000"
                    },
                    {
                        "number": "11",
                        "title": "Music Reach",
                        "duration": "256000"
                    },
                    {
                        "number": "12",
                        "title": "Jericho",
                        "duration": "228000"
                    },
                    {
                        "number": "13",
                        "title": "Funky Shit",
                        "duration": "320000"
                    },
                    {
                        "number": "14",
                        "title": "Mindfields",
                        "duration": "343000"
                    },
                    {
                        "number": "15",
                        "title": "Shoot Down",
                        "duration": "273000"
                    },
                    {
                        "number": "16",
                        "title": "Fuel My Fire",
                        "duration": "258000"
                    }
                ]
            },
            {
                "id": "2351942",
                "title": "The Dirtchamber Sessions, Volume One",
                "year": "1999",
                "genre": "Electronic",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Section 1: Intro Beats / Punk Shock / Untitled / Chemical Beats / Kool Keith Housing Things / Sport / Give the Drummer Some / Wildstyle",
                        "duration": "438200"
                    },
                    {
                        "number": "2",
                        "title": "Section 2: Bug Powder Dust / Pump Me Up / How High / Poison / Been Caught Stealing / I Get Wrecked",
                        "duration": "404960"
                    },
                    {
                        "number": "3",
                        "title": "Section 3: The Mexican / Rock the House / The Best Part of Breaking Up / King Kut",
                        "duration": "363640"
                    },
                    {
                        "number": "5",
                        "title": "Section 5: New York / Punk to Funk / I\u2019m Sick",
                        "duration": "297466"
                    },
                    {
                        "number": "7",
                        "title": "Section 7: Get Down / Humpty Dance / Dope On Plastic / Beats and Pieces",
                        "duration": "239773"
                    },
                    {
                        "number": "8",
                        "title": "Section 8: Sure Shot / Breakdance Electric Boogie / Doomsday of Rap / Ozone Breakdown / Funky Nassau / It\u2019s Just Begun",
                        "duration": "520733"
                    }
                ]
            },
            {
                "id": "2358377",
                "title": "Greatest Hits",
                "year": "2006",
                "genre": '',
                "tracks": [
                    {
                        "number": "1",
                        "title": "Girls",
                        "duration": "249000"
                    },
                    {
                        "number": "2",
                        "title": "Spitfire",
                        "duration": "309000"
                    },
                    {
                        "number": "3",
                        "title": "Breathe",
                        "duration": "336000"
                    },
                    {
                        "number": "4",
                        "title": "Smack My Bitch Up",
                        "duration": "344000"
                    },
                    {
                        "number": "5",
                        "title": "Diesel Power",
                        "duration": "258000"
                    },
                    {
                        "number": "6",
                        "title": "You\u2019ll Be Under My Wheels",
                        "duration": "237000"
                    },
                    {
                        "number": "7",
                        "title": "Funky Shit",
                        "duration": "318000"
                    },
                    {
                        "number": "8",
                        "title": "Mindfields",
                        "duration": "341000"
                    },
                    {
                        "number": "9",
                        "title": "Narayan",
                        "duration": "547000"
                    },
                    {
                        "number": "10",
                        "title": "Wake Up Call",
                        "duration": "298000"
                    },
                    {
                        "number": "11",
                        "title": "Firestarter",
                        "duration": "281000"
                    },
                    {
                        "number": "12",
                        "title": "Hotride",
                        "duration": "278000"
                    },
                    {
                        "number": "13",
                        "title": "Shoot Down",
                        "duration": "271000"
                    },
                    {
                        "number": "14",
                        "title": "Serial Thrilla",
                        "duration": "313000"
                    },
                    {
                        "number": "15",
                        "title": "Fuel My Fire",
                        "duration": "258000"
                    },
                    {
                        "number": "1",
                        "title": "Out of Space",
                        "duration": "296000"
                    },
                    {
                        "number": "2",
                        "title": "No Good",
                        "duration": "381000"
                    },
                    {
                        "number": "3",
                        "title": "Voodoo People",
                        "duration": "389000"
                    },
                    {
                        "number": "4",
                        "title": "Charly",
                        "duration": "314000"
                    },
                    {
                        "number": "5",
                        "title": "One Love",
                        "duration": "327000"
                    },
                    {
                        "number": "6",
                        "title": "Wind It Up",
                        "duration": "274000"
                    },
                    {
                        "number": "7",
                        "title": "Your Love",
                        "duration": "329000"
                    },
                    {
                        "number": "8",
                        "title": "Everybody in the Place",
                        "duration": "309000"
                    },
                    {
                        "number": "9",
                        "title": "Music Reach (1/2/3/4)",
                        "duration": "254000"
                    },
                    {
                        "number": "10",
                        "title": "Jericho",
                        "duration": "225000"
                    },
                    {
                        "number": "11",
                        "title": "Poison",
                        "duration": "406000"
                    },
                    {
                        "number": "12",
                        "title": "Their Law",
                        "duration": "338000"
                    },
                    {
                        "number": "13",
                        "title": "Leave You Far Behind",
                        "duration": "194000"
                    },
                    {
                        "number": "14",
                        "title": "Baby's Got a Temper (original version)",
                        "duration": "267000"
                    },
                    {
                        "number": "15",
                        "title": "Voodoo People (Pendulum remix)",
                        "duration": "307000"
                    }
                ]
            }
        ]
    },
    "Nirvana": {
        "albums": [
            {
                "id": "2110839",
                "title": "Nevermind",
                "year": "1991",
                "genre": "Grunge",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Smells Like Teen Spirit",
                        "duration": "301000"
                    },
                    {
                        "number": "2",
                        "title": "In Bloom",
                        "duration": "254000"
                    },
                    {
                        "number": "3",
                        "title": "Come as You Are",
                        "duration": "219000"
                    },
                    {
                        "number": "4",
                        "title": "Breed",
                        "duration": "183000"
                    },
                    {
                        "number": "5",
                        "title": "Lithium",
                        "duration": "256000"
                    },
                    {
                        "number": "6",
                        "title": "Polly",
                        "duration": "176000"
                    },
                    {
                        "number": "7",
                        "title": "Territorial Pissings",
                        "duration": "143000"
                    },
                    {
                        "number": "8",
                        "title": "Drain You",
                        "duration": "223000"
                    },
                    {
                        "number": "9",
                        "title": "Lounge Act",
                        "duration": "156000"
                    },
                    {
                        "number": "10",
                        "title": "Stay Away",
                        "duration": "212000"
                    },
                    {
                        "number": "11",
                        "title": "On a Plain",
                        "duration": "196000"
                    },
                    {
                        "number": "12",
                        "title": "Something in the Way",
                        "duration": "228000"
                    },
                    {
                        "number": "13",
                        "title": "Endless, Nameless",
                        "duration": "404000"
                    }
                ]
            },
            {
                "id": "2110840",
                "title": "In Utero",
                "year": "1993",
                "genre": "Grunge",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Serve the Servants",
                        "duration": "216200"
                    },
                    {
                        "number": "2",
                        "title": "Scentless Apprentice",
                        "duration": "227666"
                    },
                    {
                        "number": "3",
                        "title": "Heart-Shaped Box",
                        "duration": "281506"
                    },
                    {
                        "number": "4",
                        "title": "Rape Me",
                        "duration": "169826"
                    },
                    {
                        "number": "5",
                        "title": "Frances Farmer Will Have Her Revenge on Seattle",
                        "duration": "249600"
                    },
                    {
                        "number": "6",
                        "title": "Dumb",
                        "duration": "152133"
                    },
                    {
                        "number": "7",
                        "title": "Very Ape",
                        "duration": "115666"
                    },
                    {
                        "number": "8",
                        "title": "Milk It",
                        "duration": "234800"
                    },
                    {
                        "number": "9",
                        "title": "Pennyroyal Tea",
                        "duration": "217173"
                    },
                    {
                        "number": "10",
                        "title": "Radio Friendly Unit Shifter",
                        "duration": "291066"
                    },
                    {
                        "number": "11",
                        "title": "tourette's",
                        "duration": "95293"
                    },
                    {
                        "number": "12",
                        "title": "All Apologies",
                        "duration": "229773"
                    }
                ]
            },
            {
                "id": "2110841",
                "title": "Bleach",
                "year": "1989",
                "genre": "Grunge",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Blew",
                        "duration": "175000"
                    },
                    {
                        "number": "2",
                        "title": "Floyd the Barber",
                        "duration": "138000"
                    },
                    {
                        "number": "3",
                        "title": "About a Girl",
                        "duration": "168000"
                    },
                    {
                        "number": "4",
                        "title": "School",
                        "duration": "163000"
                    },
                    {
                        "number": "5",
                        "title": "Love Buzz",
                        "duration": "155000"
                    },
                    {
                        "number": "6",
                        "title": "Paper Cuts",
                        "duration": "246000"
                    },
                    {
                        "number": "7",
                        "title": "Negative Creep",
                        "duration": "175000"
                    },
                    {
                        "number": "8",
                        "title": "Scoff",
                        "duration": "250000"
                    },
                    {
                        "number": "9",
                        "title": "Swap Meet",
                        "duration": "183000"
                    },
                    {
                        "number": "10",
                        "title": "Mr. Moustache",
                        "duration": "204000"
                    },
                    {
                        "number": "11",
                        "title": "Sifting",
                        "duration": "324000"
                    },
                    {
                        "number": "12",
                        "title": "Big Cheese",
                        "duration": "222000"
                    },
                    {
                        "number": "13",
                        "title": "Downer",
                        "duration": "104000"
                    }
                ]
            },
            {
                "id": "2118194",
                "title": "MTV Unplugged in New York",
                "year": "1994",
                "genre": "Grunge",
                "tracks": [
                    {
                        "number": "1",
                        "title": "About a Girl",
                        "duration": "218000"
                    },
                    {
                        "number": "2",
                        "title": "Come as You Are",
                        "duration": "253893"
                    },
                    {
                        "number": "3",
                        "title": "Jesus Doesn't Want Me for a Sunbeam",
                        "duration": "277266"
                    },
                    {
                        "number": "4",
                        "title": "The Man Who Sold the World",
                        "duration": "261106"
                    },
                    {
                        "number": "5",
                        "title": "Pennyroyal Tea",
                        "duration": "220493"
                    },
                    {
                        "number": "6",
                        "title": "Dumb",
                        "duration": "172933"
                    },
                    {
                        "number": "7",
                        "title": "Polly",
                        "duration": "196466"
                    },
                    {
                        "number": "8",
                        "title": "On a Plain",
                        "duration": "224733"
                    },
                    {
                        "number": "9",
                        "title": "Something in the Way",
                        "duration": "241533"
                    },
                    {
                        "number": "10",
                        "title": "Plateau",
                        "duration": "218133"
                    },
                    {
                        "number": "11",
                        "title": "Oh Me",
                        "duration": "206173"
                    },
                    {
                        "number": "12",
                        "title": "Lake of Fire",
                        "duration": "175960"
                    },
                    {
                        "number": "13",
                        "title": "All Apologies",
                        "duration": "263240"
                    },
                    {
                        "number": "14",
                        "title": "Where Did You Sleep Last Night?",
                        "duration": "306066"
                    }
                ]
            },
            {
                "id": "2118557",
                "title": "Nirvana",
                "year": "2002",
                "genre": "Grunge",
                "tracks": [
                    {
                        "number": "1",
                        "title": "You Know You're Right",
                        "duration": "218026"
                    },
                    {
                        "number": "2",
                        "title": "About a Girl",
                        "duration": "169173"
                    },
                    {
                        "number": "3",
                        "title": "Been a Son",
                        "duration": "143933"
                    },
                    {
                        "number": "4",
                        "title": "Sliver",
                        "duration": "134026"
                    },
                    {
                        "number": "5",
                        "title": "Smells Like Teen Spirit",
                        "duration": "301333"
                    },
                    {
                        "number": "6",
                        "title": "Come as You Are",
                        "duration": "219040"
                    },
                    {
                        "number": "7",
                        "title": "Lithium",
                        "duration": "257160"
                    },
                    {
                        "number": "8",
                        "title": "In Bloom",
                        "duration": "254973"
                    },
                    {
                        "number": "9",
                        "title": "Heart-Shaped Box",
                        "duration": "282466"
                    },
                    {
                        "number": "10",
                        "title": "Pennyroyal Tea (Scott Litt mix)",
                        "duration": "217666"
                    },
                    {
                        "number": "11",
                        "title": "Rape Me",
                        "duration": "171333"
                    },
                    {
                        "number": "12",
                        "title": "Dumb",
                        "duration": "154400"
                    },
                    {
                        "number": "13",
                        "title": "All Apologies",
                        "duration": "227960"
                    },
                    {
                        "number": "14",
                        "title": "The Man Who Sold the World",
                        "duration": "227440"
                    }
                ]
            },
            {
                "id": "2118558",
                "title": "Live at Reading",
                "year": "2009",
                "genre": "Grunge",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Breed",
                        "duration": "192080"
                    },
                    {
                        "number": "2",
                        "title": "Drain You",
                        "duration": "218440"
                    },
                    {
                        "number": "3",
                        "title": "Aneurysm",
                        "duration": "275026"
                    },
                    {
                        "number": "4",
                        "title": "School",
                        "duration": "163280"
                    },
                    {
                        "number": "5",
                        "title": "Sliver",
                        "duration": "126120"
                    },
                    {
                        "number": "6",
                        "title": "In Bloom",
                        "duration": "276160"
                    },
                    {
                        "number": "7",
                        "title": "Come as You Are",
                        "duration": "216333"
                    },
                    {
                        "number": "8",
                        "title": "Lithium",
                        "duration": "261813"
                    },
                    {
                        "number": "9",
                        "title": "About a Girl",
                        "duration": "171960"
                    },
                    {
                        "number": "10",
                        "title": "Tourette's",
                        "duration": "110573"
                    },
                    {
                        "number": "11",
                        "title": "Polly",
                        "duration": "168626"
                    },
                    {
                        "number": "12",
                        "title": "Lounge Act",
                        "duration": "156786"
                    },
                    {
                        "number": "13",
                        "title": "Smells Like Teen Spirit",
                        "duration": "285186"
                    },
                    {
                        "number": "14",
                        "title": "On a Plain",
                        "duration": "180293"
                    },
                    {
                        "number": "15",
                        "title": "Negative Creep",
                        "duration": "172440"
                    },
                    {
                        "number": "16",
                        "title": "Been a Son",
                        "duration": "133426"
                    },
                    {
                        "number": "17",
                        "title": "All Apologies",
                        "duration": "189853"
                    },
                    {
                        "number": "18",
                        "title": "Blew",
                        "duration": "199720"
                    },
                    {
                        "number": "19",
                        "title": "Dumb",
                        "duration": "152400"
                    },
                    {
                        "number": "20",
                        "title": "Stay Away",
                        "duration": "212933"
                    },
                    {
                        "number": "21",
                        "title": "Spank Thru",
                        "duration": "186866"
                    },
                    {
                        "number": "22",
                        "title": "The Money Will Roll Right In",
                        "duration": "136560"
                    },
                    {
                        "number": "23",
                        "title": "D-7",
                        "duration": "223826"
                    },
                    {
                        "number": "24",
                        "title": "Territorial Pissings",
                        "duration": "269826"
                    }
                ]
            },
            {
                "id": "2126486",
                "title": "The Very Best",
                "year": "1994",
                "genre": "Grunge",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Smells Like Teen Spirit",
                        "duration": "302840"
                    },
                    {
                        "number": "2",
                        "title": "Come as You Are",
                        "duration": "221333"
                    },
                    {
                        "number": "3",
                        "title": "Oh, the Guilt",
                        "duration": "204026"
                    },
                    {
                        "number": "4",
                        "title": "Dive",
                        "duration": "234133"
                    },
                    {
                        "number": "5",
                        "title": "Aero Zeppelin",
                        "duration": "280666"
                    },
                    {
                        "number": "6",
                        "title": "Heart-Shaped Box",
                        "duration": "281706"
                    },
                    {
                        "number": "7",
                        "title": "Puss",
                        "duration": "201466"
                    },
                    {
                        "number": "8",
                        "title": "In Bloom",
                        "duration": "255733"
                    },
                    {
                        "number": "9",
                        "title": "Sliver",
                        "duration": "133266"
                    },
                    {
                        "number": "10",
                        "title": "Frances Farmer Will Have Her Revenge on Seattle",
                        "duration": "249826"
                    },
                    {
                        "number": "11",
                        "title": "Drain You",
                        "duration": "226106"
                    },
                    {
                        "number": "12",
                        "title": "Lithium",
                        "duration": "258760"
                    },
                    {
                        "number": "13",
                        "title": "All Apologies",
                        "duration": "232400"
                    },
                    {
                        "number": "14",
                        "title": "Big Long Now",
                        "duration": "114866"
                    },
                    {
                        "number": "15",
                        "title": "Stay Away",
                        "duration": "213133"
                    },
                    {
                        "number": "16",
                        "title": "Aneurysm",
                        "duration": "276800"
                    },
                    {
                        "number": "17",
                        "title": "Rape Me",
                        "duration": "171040"
                    },
                    {
                        "number": "18",
                        "title": "School",
                        "duration": "146226"
                    },
                    {
                        "number": "19",
                        "title": "Floyd the Barber",
                        "duration": "140400"
                    },
                    {
                        "number": "20",
                        "title": "About a Girl",
                        "duration": "175333"
                    },
                    {
                        "number": "21",
                        "title": "Breed",
                        "duration": "184266"
                    }
                ]
            },
            {
                "id": "2127060",
                "title": "Incesticide",
                "year": "1992",
                "genre": "Grunge",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Dive",
                        "duration": "235000"
                    },
                    {
                        "number": "2",
                        "title": "Sliver",
                        "duration": "136000"
                    },
                    {
                        "number": "3",
                        "title": "Stain",
                        "duration": "160000"
                    },
                    {
                        "number": "4",
                        "title": "Been a Son",
                        "duration": "115000"
                    },
                    {
                        "number": "5",
                        "title": "Turnaround",
                        "duration": "139000"
                    },
                    {
                        "number": "6",
                        "title": "Molly's Lips",
                        "duration": "114000"
                    },
                    {
                        "number": "7",
                        "title": "Son of a Gun",
                        "duration": "168000"
                    },
                    {
                        "number": "8",
                        "title": "(New Wave) Polly",
                        "duration": "108000"
                    },
                    {
                        "number": "9",
                        "title": "Beeswax",
                        "duration": "170000"
                    },
                    {
                        "number": "10",
                        "title": "Downer",
                        "duration": "103000"
                    },
                    {
                        "number": "11",
                        "title": "Mexican Seafood",
                        "duration": "115000"
                    },
                    {
                        "number": "12",
                        "title": "Hairspray Queen",
                        "duration": "253000"
                    },
                    {
                        "number": "13",
                        "title": "Aero Zeppelin",
                        "duration": "281000"
                    },
                    {
                        "number": "14",
                        "title": "Big Long Now",
                        "duration": "303000"
                    },
                    {
                        "number": "15",
                        "title": "Aneurysm",
                        "duration": "275000"
                    }
                ]
            },
            {
                "id": "2145493",
                "title": "From the Muddy Banks of the Wishkah",
                "year": "1996",
                "genre": "Grunge",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Intro",
                        "duration": "52626"
                    },
                    {
                        "number": "2",
                        "title": "School",
                        "duration": "160040"
                    },
                    {
                        "number": "3",
                        "title": "Drain You",
                        "duration": "215093"
                    },
                    {
                        "number": "4",
                        "title": "Aneurysm",
                        "duration": "271466"
                    },
                    {
                        "number": "5",
                        "title": "Smells Like Teen Spirit",
                        "duration": "287040"
                    },
                    {
                        "number": "6",
                        "title": "Been a Son",
                        "duration": "127493"
                    },
                    {
                        "number": "7",
                        "title": "Lithium",
                        "duration": "249866"
                    },
                    {
                        "number": "8",
                        "title": "Sliver",
                        "duration": "116200"
                    },
                    {
                        "number": "9",
                        "title": "Spank Thru",
                        "duration": "190266"
                    },
                    {
                        "number": "10",
                        "title": "Scentless Apprentice",
                        "duration": "211066"
                    },
                    {
                        "number": "11",
                        "title": "Heart\u2010Shaped Box",
                        "duration": "281866"
                    },
                    {
                        "number": "12",
                        "title": "Milk It",
                        "duration": "225440"
                    },
                    {
                        "number": "13",
                        "title": "Negative Creep",
                        "duration": "163826"
                    },
                    {
                        "number": "14",
                        "title": "Polly",
                        "duration": "149866"
                    },
                    {
                        "number": "15",
                        "title": "Breed",
                        "duration": "208466"
                    },
                    {
                        "number": "16",
                        "title": "tourette's",
                        "duration": "115373"
                    },
                    {
                        "number": "17",
                        "title": "Blew",
                        "duration": "218400"
                    }
                ]
            },
            {
                "id": "2145494",
                "title": "With the Lights Out",
                "year": "2004",
                "genre": "Grunge",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Heartbreaker",
                        "duration": "179560"
                    },
                    {
                        "number": "2",
                        "title": "Anorexorcist (radio performance, 1987)",
                        "duration": "164773"
                    },
                    {
                        "number": "3",
                        "title": "White Lace and Strange (radio performance, 1987)",
                        "duration": "129066"
                    },
                    {
                        "number": "4",
                        "title": "Help Me I'm Hungry (radio performance, 1987)",
                        "duration": "161560"
                    },
                    {
                        "number": "5",
                        "title": "Mrs. Butterworth (rehearsal recording, 1988)",
                        "duration": "245106"
                    },
                    {
                        "number": "6",
                        "title": "If You Must (demo, 1988)",
                        "duration": "241066"
                    },
                    {
                        "number": "7",
                        "title": "Pen Cap Chew (demo, 1988)",
                        "duration": "182066"
                    },
                    {
                        "number": "8",
                        "title": "Downer",
                        "duration": "103066"
                    },
                    {
                        "number": "9",
                        "title": "Floyd the Barber",
                        "duration": "153026"
                    },
                    {
                        "number": "10",
                        "title": "Raunchola / Moby Dick",
                        "duration": "384666"
                    },
                    {
                        "number": "11",
                        "title": "Beans (solo acoustic, undated)",
                        "duration": "92573"
                    },
                    {
                        "number": "12",
                        "title": "Don't Want It All (solo acoustic, undated)",
                        "duration": "146293"
                    },
                    {
                        "number": "13",
                        "title": "Clean Up Before She Comes (solo acoustic, undated)",
                        "duration": "192506"
                    },
                    {
                        "number": "14",
                        "title": "Polly (solo acoustic, 1988)",
                        "duration": "150226"
                    },
                    {
                        "number": "15",
                        "title": "About a Girl (solo acoustic, 1988)",
                        "duration": "164800"
                    },
                    {
                        "number": "16",
                        "title": "Blandest (demo, 1988)",
                        "duration": "236106"
                    },
                    {
                        "number": "17",
                        "title": "Dive (demo, 1988)",
                        "duration": "290600"
                    },
                    {
                        "number": "18",
                        "title": "They Hung Him on a Cross (demo, 1989)",
                        "duration": "117400"
                    },
                    {
                        "number": "19",
                        "title": "Grey Goose (demo, 1989)",
                        "duration": "276360"
                    },
                    {
                        "number": "20",
                        "title": "Ain't It a Shame (demo, 1989)",
                        "duration": "121840"
                    },
                    {
                        "number": "21",
                        "title": "Token Eastern Song (demo, 1989)",
                        "duration": "201360"
                    },
                    {
                        "number": "22",
                        "title": "Even in His Youth (demo, 1989)",
                        "duration": "192866"
                    },
                    {
                        "number": "23",
                        "title": "Polly (demo, 1989)",
                        "duration": "156866"
                    },
                    {
                        "number": "1",
                        "title": "Opinion (solo acoustic, 1990)",
                        "duration": "94426"
                    },
                    {
                        "number": "2",
                        "title": "Lithium (solo acoustic, 1990)",
                        "duration": "109440"
                    },
                    {
                        "number": "3",
                        "title": "Been a Son (solo acoustic, 1990)",
                        "duration": "72760"
                    },
                    {
                        "number": "4",
                        "title": "Sliver (solo acoustic, 1989)",
                        "duration": "129906"
                    },
                    {
                        "number": "5",
                        "title": "Where Did You Sleep Last Night? (solo acoustic, 1989)",
                        "duration": "151533"
                    },
                    {
                        "number": "6",
                        "title": "Pay to Play (demo, 1990)",
                        "duration": "209333"
                    },
                    {
                        "number": "7",
                        "title": "Here She Comes Now (demo, 1990)",
                        "duration": "301533"
                    },
                    {
                        "number": "8",
                        "title": "Drain You (demo, 1990)",
                        "duration": "158400"
                    },
                    {
                        "number": "9",
                        "title": "Aneurysm (demo, 1990)",
                        "duration": "287693"
                    },
                    {
                        "number": "10",
                        "title": "Smells Like Teen Spirit (rehearsal demo, 1991)",
                        "duration": "340533"
                    },
                    {
                        "number": "11",
                        "title": "Breed (Rough mix, 1991)",
                        "duration": "187733"
                    },
                    {
                        "number": "12",
                        "title": "Verse Chorus Verse (outtake, 1991)",
                        "duration": "198000"
                    },
                    {
                        "number": "13",
                        "title": "Old Age (outtake, 1991)",
                        "duration": "260466"
                    },
                    {
                        "number": "14",
                        "title": "Endless, Nameless (radio appearance, 1991)",
                        "duration": "528000"
                    },
                    {
                        "number": "15",
                        "title": "Dumb (radio appearance, 1991)",
                        "duration": "155373"
                    },
                    {
                        "number": "16",
                        "title": "D-7 (radio appearance, 1990)",
                        "duration": "226560"
                    },
                    {
                        "number": "17",
                        "title": "Oh, the Guilt (B-side, 1992)",
                        "duration": "205706"
                    },
                    {
                        "number": "18",
                        "title": "Curmudgeon (B-side, 1992)",
                        "duration": "183600"
                    },
                    {
                        "number": "19",
                        "title": "Return of the Rat (Outtake, 1992)",
                        "duration": "189333"
                    },
                    {
                        "number": "20",
                        "title": "Smells Like Teen Spirit (Butch Vig mix)",
                        "duration": "299160"
                    },
                    {
                        "number": "1",
                        "title": "Rape Me (solo acoustic, 1992)",
                        "duration": "203400"
                    },
                    {
                        "number": "2",
                        "title": "Rape Me (demo, 1992)",
                        "duration": "181826"
                    },
                    {
                        "number": "3",
                        "title": "Scentless Apprentice (rehearsal demo, 1992)",
                        "duration": "572906"
                    },
                    {
                        "number": "4",
                        "title": "Heart-Shaped Box (demo, 1993)",
                        "duration": "331893"
                    },
                    {
                        "number": "5",
                        "title": "I Hate Myself and I Want to Die (B-side, 1993)",
                        "duration": "243400"
                    },
                    {
                        "number": "6",
                        "title": "Milk It (demo, 1993)",
                        "duration": "274666"
                    },
                    {
                        "number": "7",
                        "title": "Moist Vagina (demo, 1993)",
                        "duration": "116906"
                    },
                    {
                        "number": "8",
                        "title": "Gallons of Rubbing Alcohol Flow Through the Strip (B-side, 1993)",
                        "duration": "454000"
                    },
                    {
                        "number": "9",
                        "title": "The Other Improv (demo, 1993)",
                        "duration": "384493"
                    },
                    {
                        "number": "10",
                        "title": "Serve the Servants (solo acoustic, 1993)",
                        "duration": "96200"
                    },
                    {
                        "number": "11",
                        "title": "Very Ape (solo acoustic, 1993)",
                        "duration": "112666"
                    },
                    {
                        "number": "12",
                        "title": "Pennyroyal Tea (solo acoustic, 1993)",
                        "duration": "210333"
                    },
                    {
                        "number": "13",
                        "title": "Marigold",
                        "duration": "154173"
                    },
                    {
                        "number": "14",
                        "title": "Sappy (B-side, 1993)",
                        "duration": "206626"
                    },
                    {
                        "number": "15",
                        "title": "Jesus Doesn't Want Me for a Sunbeam (rehearsal demo, 1994)",
                        "duration": "237506"
                    },
                    {
                        "number": "16",
                        "title": "Do Re Mi (solo acoustic, 1994)",
                        "duration": "264693"
                    },
                    {
                        "number": "17",
                        "title": "You Know You're Right (solo acoustic, 1994)",
                        "duration": "150800"
                    },
                    {
                        "number": "18",
                        "title": "All Apologies (solo acoustic, undated)",
                        "duration": "213440"
                    },
                    {
                        "number": "1",
                        "title": "Love Buzz",
                        "duration": "153000"
                    },
                    {
                        "number": "2",
                        "title": "Scoff",
                        "duration": "28000"
                    },
                    {
                        "number": "3",
                        "title": "About a Girl",
                        "duration": "185000"
                    },
                    {
                        "number": "4",
                        "title": "Big Long Now",
                        "duration": "261000"
                    },
                    {
                        "number": "5",
                        "title": "Immigrant Song",
                        "duration": "117000"
                    },
                    {
                        "number": "6",
                        "title": "Spank Thru",
                        "duration": "183000"
                    },
                    {
                        "number": "7",
                        "title": "Hairspray Queen",
                        "duration": "218000"
                    },
                    {
                        "number": "8",
                        "title": "School",
                        "duration": "174000"
                    },
                    {
                        "number": "9",
                        "title": "Mr. Moustache",
                        "duration": "227000"
                    },
                    {
                        "number": "10",
                        "title": "Big Cheese",
                        "duration": "195000"
                    },
                    {
                        "number": "11",
                        "title": "Sappy",
                        "duration": "268000"
                    },
                    {
                        "number": "12",
                        "title": "In Bloom",
                        "duration": "271000"
                    },
                    {
                        "number": "13",
                        "title": "School",
                        "duration": "153000"
                    },
                    {
                        "number": "14",
                        "title": "Love Buzz",
                        "duration": "221000"
                    },
                    {
                        "number": "15",
                        "title": "Pennyroyal Tea",
                        "duration": "115000"
                    },
                    {
                        "number": "16",
                        "title": "Smells Like Teen Spirit",
                        "duration": "377000"
                    },
                    {
                        "number": "17",
                        "title": "Territorial Pissings",
                        "duration": "165000"
                    },
                    {
                        "number": "18",
                        "title": "Jesus Doesn't Want Me for a Sunbeam",
                        "duration": "211000"
                    },
                    {
                        "number": "19",
                        "title": "Talk to Me",
                        "duration": "213000"
                    },
                    {
                        "number": "20",
                        "title": "Seasons in the Sun",
                        "duration": "202000"
                    }
                ]
            },
            {
                "id": "2205521",
                "title": "Singles",
                "year": "1995",
                "genre": "Grunge",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Smells Like Teen Spirit (edit)",
                        "duration": "279413"
                    },
                    {
                        "number": "2",
                        "title": "Even in His Youth",
                        "duration": "186413"
                    },
                    {
                        "number": "3",
                        "title": "Aneurysm",
                        "duration": "290280"
                    },
                    {
                        "number": "4",
                        "title": "Come as You Are",
                        "duration": "222000"
                    },
                    {
                        "number": "5",
                        "title": "Endless, Nameless",
                        "duration": "406573"
                    },
                    {
                        "number": "6",
                        "title": "School",
                        "duration": "158120"
                    },
                    {
                        "number": "7",
                        "title": "Drain You",
                        "duration": "232546"
                    },
                    {
                        "number": "8",
                        "title": "In Bloom (LP version)",
                        "duration": "257413"
                    },
                    {
                        "number": "9",
                        "title": "Sliver",
                        "duration": "126333"
                    },
                    {
                        "number": "10",
                        "title": "Polly",
                        "duration": "170640"
                    },
                    {
                        "number": "11",
                        "title": "Lithium (LP version)",
                        "duration": "259373"
                    },
                    {
                        "number": "12",
                        "title": "Been A Son (live)",
                        "duration": "153733"
                    },
                    {
                        "number": "13",
                        "title": "Curmudgeon",
                        "duration": "181213"
                    },
                    {
                        "number": "14",
                        "title": "Heart-Shaped Box",
                        "duration": "280746"
                    },
                    {
                        "number": "15",
                        "title": "Milk It (LP version)",
                        "duration": "234173"
                    },
                    {
                        "number": "16",
                        "title": "Marigold",
                        "duration": "157000"
                    },
                    {
                        "number": "17",
                        "title": "All Apologies (LP version)",
                        "duration": "230306"
                    },
                    {
                        "number": "18",
                        "title": "Rape Me (LP version)",
                        "duration": "170426"
                    },
                    {
                        "number": "19",
                        "title": "Moist Vagina",
                        "duration": "215693"
                    },
                    {
                        "number": "20",
                        "title": "Where Did You Sleep Last Night?",
                        "duration": "308880"
                    }
                ]
            },
            {
                "id": "2208661",
                "title": "Sliver: The Best of the Box",
                "year": "2005",
                "genre": "Grunge",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Spank Thru (1985 Fecal Matter demo)",
                        "duration": "225333"
                    },
                    {
                        "number": "2",
                        "title": "Heartbreaker",
                        "duration": "179160"
                    },
                    {
                        "number": "3",
                        "title": "Mrs. Butterworth (rehearsal demo)",
                        "duration": "244866"
                    },
                    {
                        "number": "4",
                        "title": "Floyd the Barber",
                        "duration": "153040"
                    },
                    {
                        "number": "5",
                        "title": "Clean Up Before She Comes (home demo)",
                        "duration": "192600"
                    },
                    {
                        "number": "6",
                        "title": "About a Girl (home demo)",
                        "duration": "164733"
                    },
                    {
                        "number": "7",
                        "title": "Blandest (studio demo)",
                        "duration": "236666"
                    },
                    {
                        "number": "8",
                        "title": "Ain't It a Shame (studio demo)",
                        "duration": "123000"
                    },
                    {
                        "number": "9",
                        "title": "Sappy (1990 studio demo)",
                        "duration": "213400"
                    },
                    {
                        "number": "10",
                        "title": "Opinion (solo acoustic radio appearance)",
                        "duration": "95093"
                    },
                    {
                        "number": "11",
                        "title": "Lithium (solo acoustic radio appearance)",
                        "duration": "109506"
                    },
                    {
                        "number": "12",
                        "title": "Sliver (home demo)",
                        "duration": "130360"
                    },
                    {
                        "number": "13",
                        "title": "Smells Like Teen Spirit (boom box version)",
                        "duration": "340840"
                    },
                    {
                        "number": "14",
                        "title": "Come as You Are (boom box version)",
                        "duration": "250760"
                    },
                    {
                        "number": "15",
                        "title": "Old Age (Nevermind outtake)",
                        "duration": "261133"
                    },
                    {
                        "number": "16",
                        "title": "Oh, the Guilt",
                        "duration": "205640"
                    },
                    {
                        "number": "17",
                        "title": "Rape Me (home demo)",
                        "duration": "203226"
                    },
                    {
                        "number": "18",
                        "title": "Rape Me (band demo)",
                        "duration": "183306"
                    },
                    {
                        "number": "19",
                        "title": "Heart Shaped Box (band demo)",
                        "duration": "333000"
                    },
                    {
                        "number": "20",
                        "title": "Do Re Mi (home demo)",
                        "duration": "264693"
                    },
                    {
                        "number": "21",
                        "title": "You Know You're Right (home demo)",
                        "duration": "150573"
                    },
                    {
                        "number": "22",
                        "title": "All Apologies (home demo)",
                        "duration": "213400"
                    }
                ]
            },
            {
                "id": "2240274",
                "title": "Verse Chorus Verse",
                "year": "1994",
                "genre": "Grunge",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Love Buzz",
                        "duration": "0"
                    },
                    {
                        "number": "2",
                        "title": "Return of the Rat",
                        "duration": "0"
                    },
                    {
                        "number": "3",
                        "title": "Stay Away",
                        "duration": "0"
                    },
                    {
                        "number": "4",
                        "title": "Oh, the Guilt",
                        "duration": "0"
                    },
                    {
                        "number": "5",
                        "title": "I Hate Myself and Want to Die",
                        "duration": "0"
                    },
                    {
                        "number": "6",
                        "title": "Curmudgeon",
                        "duration": "0"
                    },
                    {
                        "number": "7",
                        "title": "Dive",
                        "duration": "0"
                    },
                    {
                        "number": "8",
                        "title": "Jesus Don't Want Me for a Sunbeam",
                        "duration": "0"
                    },
                    {
                        "number": "9",
                        "title": "Spank Thru",
                        "duration": "0"
                    },
                    {
                        "number": "10",
                        "title": "Sappy (Verse Chorus Verse)",
                        "duration": "0"
                    },
                    {
                        "number": "11",
                        "title": "Here She Comes Now",
                        "duration": "0"
                    },
                    {
                        "number": "12",
                        "title": "Dumb",
                        "duration": "0"
                    }
                ]
            },
            {
                "id": "2251549",
                "title": "Unreleased Tracks",
                "year": "2000",
                "genre": "Grunge",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Return of the Rat",
                        "duration": "194240"
                    },
                    {
                        "number": "2",
                        "title": "Aneurysm",
                        "duration": "290333"
                    },
                    {
                        "number": "3",
                        "title": "Even in His Youth",
                        "duration": "188666"
                    },
                    {
                        "number": "4",
                        "title": "Marigold",
                        "duration": "161333"
                    },
                    {
                        "number": "5",
                        "title": "D-7",
                        "duration": "233666"
                    },
                    {
                        "number": "6",
                        "title": "Curmudgeon",
                        "duration": "184000"
                    },
                    {
                        "number": "7",
                        "title": "Gallons of Rubbing Alcohol Flow Through the Strip",
                        "duration": "457333"
                    },
                    {
                        "number": "8",
                        "title": "I Hate Myself and Want to Die",
                        "duration": "165666"
                    },
                    {
                        "number": "9",
                        "title": "Here She Comes Now",
                        "duration": "302000"
                    },
                    {
                        "number": "10",
                        "title": "Oh, the Guilt",
                        "duration": "204333"
                    },
                    {
                        "number": "11",
                        "title": "Do You Love Me?",
                        "duration": "218000"
                    },
                    {
                        "number": "12",
                        "title": "Moist Vagina",
                        "duration": "218666"
                    },
                    {
                        "number": "13",
                        "title": "Happy Hour",
                        "duration": "204333"
                    },
                    {
                        "number": "14",
                        "title": "Spank Thru",
                        "duration": "206000"
                    },
                    {
                        "number": "15",
                        "title": "Pay to Play",
                        "duration": "214000"
                    },
                    {
                        "number": "16",
                        "title": "Endless, Nameless",
                        "duration": "410000"
                    }
                ]
            },
            {
                "id": "2251552",
                "title": "Outcesticide II: The Needle & The Damage Done",
                "year": "1994",
                "genre": "Grunge",
                "tracks": [
                    {
                        "number": "1",
                        "title": "In Bloom (Unissued Sub Pop 7\" Mastertape) (5/90)",
                        "duration": "269533"
                    },
                    {
                        "number": "2",
                        "title": "Imodium (Early Version of \"Breed\" With Different Lyrics) (11/89)",
                        "duration": "183266"
                    },
                    {
                        "number": "3",
                        "title": "Vendetagainst",
                        "duration": "155133"
                    },
                    {
                        "number": "4",
                        "title": "Oh, the Guilt (live version) (11/89)",
                        "duration": "190266"
                    },
                    {
                        "number": "5",
                        "title": "Smells Like Teen Spirit (1/93)",
                        "duration": "288333"
                    },
                    {
                        "number": "6",
                        "title": "Pennyroyal Tea",
                        "duration": "254733"
                    },
                    {
                        "number": "7",
                        "title": "It's Closing Time",
                        "duration": "157733"
                    },
                    {
                        "number": "8",
                        "title": "Heart-Shaped Box (alternate lyrics)",
                        "duration": "326333"
                    },
                    {
                        "number": "9",
                        "title": "Scentless Apprentice (Extended Experimental Feedback version) (1/93)",
                        "duration": "582333"
                    },
                    {
                        "number": "10",
                        "title": "Been a Son (acoustic rehearsal) (10/91)",
                        "duration": "126600"
                    },
                    {
                        "number": "11",
                        "title": "Something in the Way (In-Store Acoustic Gig) (10/91)",
                        "duration": "200933"
                    },
                    {
                        "number": "12",
                        "title": "Negative Creep (In-Store Acoustic Gig) (10/91)",
                        "duration": "121466"
                    },
                    {
                        "number": "13",
                        "title": "Where Did You Sleep Last Night? (Kurt Solo at Castaic Lake) (9/92)",
                        "duration": "145666"
                    },
                    {
                        "number": "14",
                        "title": "Baba O'Riley (Covering The Who in Rennes) (12/91)",
                        "duration": "192733"
                    },
                    {
                        "number": "15",
                        "title": "The End (Slaughtering The Doors In Belgium) (11/91)",
                        "duration": "140600"
                    },
                    {
                        "number": "16",
                        "title": "Lithium (Mix Six, unreleased studio version) (6/91)",
                        "duration": "174666"
                    },
                    {
                        "number": "17",
                        "title": "Dumb (2/94)",
                        "duration": "143733"
                    },
                    {
                        "number": "18",
                        "title": "Molly's Lips (An Early Attempt at The Vaseline's Song) (11/89)",
                        "duration": "143266"
                    },
                    {
                        "number": "19",
                        "title": "Verse Chorus Verse",
                        "duration": "187000"
                    },
                    {
                        "number": "20",
                        "title": "The Man Who Sold the World (electric version) (12/93)",
                        "duration": "274666"
                    },
                    {
                        "number": "21",
                        "title": "Smells Like Teen Spirit (Live on the World TV Show) (11/91)",
                        "duration": "177266"
                    }
                ]
            },
            {
                "id": "2251570",
                "title": "Outcesticide: In Memory of Kurt Cobain",
                "year": "1994",
                "genre": "Grunge",
                "tracks": [
                    {
                        "number": "1",
                        "title": "If You Must",
                        "duration": "230040"
                    },
                    {
                        "number": "2",
                        "title": "Downer",
                        "duration": "97600"
                    },
                    {
                        "number": "3",
                        "title": "Floyd the Barber",
                        "duration": "129746"
                    },
                    {
                        "number": "4",
                        "title": "Paper Cuts",
                        "duration": "231920"
                    },
                    {
                        "number": "5",
                        "title": "Spank Thru",
                        "duration": "201773"
                    },
                    {
                        "number": "6",
                        "title": "Beeswax",
                        "duration": "155346"
                    },
                    {
                        "number": "7",
                        "title": "Pen Cap Chew",
                        "duration": "170733"
                    },
                    {
                        "number": "8",
                        "title": "Blandest",
                        "duration": "236440"
                    },
                    {
                        "number": "9",
                        "title": "Polly (Acoustic)",
                        "duration": "142626"
                    },
                    {
                        "number": "10",
                        "title": "Seed",
                        "duration": "144666"
                    },
                    {
                        "number": "11",
                        "title": "Sappy (acoustic)",
                        "duration": "145560"
                    },
                    {
                        "number": "12",
                        "title": "Do You Love Me?",
                        "duration": "208906"
                    },
                    {
                        "number": "13",
                        "title": "Been a Son",
                        "duration": "123960"
                    },
                    {
                        "number": "14",
                        "title": "Token Eastern Song",
                        "duration": "209293"
                    },
                    {
                        "number": "15",
                        "title": "Opinion",
                        "duration": "102240"
                    },
                    {
                        "number": "16",
                        "title": "D-7",
                        "duration": "150600"
                    },
                    {
                        "number": "17",
                        "title": "Imodium",
                        "duration": "193906"
                    },
                    {
                        "number": "18",
                        "title": "Pay to Play",
                        "duration": "209813"
                    },
                    {
                        "number": "19",
                        "title": "Sappy",
                        "duration": "208906"
                    },
                    {
                        "number": "20",
                        "title": "Here She Comes Now",
                        "duration": "283226"
                    },
                    {
                        "number": "21",
                        "title": "Where Did You Sleep Last Night?",
                        "duration": "297720"
                    },
                    {
                        "number": "22",
                        "title": "Return of the Rat",
                        "duration": "182280"
                    },
                    {
                        "number": "23",
                        "title": "Talk to Me",
                        "duration": "201533"
                    },
                    {
                        "number": "24",
                        "title": "Krist's Eulogy",
                        "duration": "55040"
                    },
                    {
                        "number": "25",
                        "title": "Courtney Love's Complete Eulogy for Kurt Cobain",
                        "duration": "378120"
                    }
                ]
            },
            {
                "id": "2251571",
                "title": "In Utero Demos",
                "year": "2001",
                "genre": "Grunge",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Rape Me",
                        "duration": "166360"
                    },
                    {
                        "number": "2",
                        "title": "Scentless Apprentice",
                        "duration": "224773"
                    },
                    {
                        "number": "3",
                        "title": "Heart\u2010Shaped Box",
                        "duration": "277866"
                    },
                    {
                        "number": "4",
                        "title": "Milk It",
                        "duration": "231800"
                    },
                    {
                        "number": "5",
                        "title": "Dumb",
                        "duration": "147693"
                    },
                    {
                        "number": "6",
                        "title": "Radio Friendly Unit Shifter",
                        "duration": "286866"
                    },
                    {
                        "number": "7",
                        "title": "Very Ape",
                        "duration": "116773"
                    },
                    {
                        "number": "8",
                        "title": "Pennyroyal Tea",
                        "duration": "211226"
                    },
                    {
                        "number": "9",
                        "title": "Frances Farmer Will Have Her Revenge on Seattle",
                        "duration": "248733"
                    },
                    {
                        "number": "10",
                        "title": "tourette's",
                        "duration": "94400"
                    },
                    {
                        "number": "11",
                        "title": "Serve the Servants",
                        "duration": "215640"
                    },
                    {
                        "number": "12",
                        "title": "All Apologies",
                        "duration": "230093"
                    },
                    {
                        "number": "13",
                        "title": "Moist Vagina",
                        "duration": "203440"
                    },
                    {
                        "number": "14",
                        "title": "Marigold",
                        "duration": "156400"
                    },
                    {
                        "number": "15",
                        "title": "Sappy",
                        "duration": "210600"
                    },
                    {
                        "number": "16",
                        "title": "I Hate Myself and Want to Die",
                        "duration": "169334"
                    }
                ]
            },
            {
                "id": "2251573",
                "title": "First Live Show",
                "year": "2001",
                "genre": "Grunge",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Downer (soundcheck)",
                        "duration": "350840"
                    },
                    {
                        "number": "2",
                        "title": "Aero Zeppelin",
                        "duration": "377973"
                    },
                    {
                        "number": "3",
                        "title": "If You Must",
                        "duration": "517840"
                    },
                    {
                        "number": "4",
                        "title": "Heartbreaker",
                        "duration": "180120"
                    },
                    {
                        "number": "5",
                        "title": "How Many More Times",
                        "duration": "106586"
                    },
                    {
                        "number": "6",
                        "title": "Mexican Seafood",
                        "duration": "177173"
                    },
                    {
                        "number": "7",
                        "title": "Pen Cap Chew",
                        "duration": "338026"
                    },
                    {
                        "number": "8",
                        "title": "Spank Thru",
                        "duration": "362866"
                    },
                    {
                        "number": "9",
                        "title": "Hairspray Queen",
                        "duration": "355760"
                    },
                    {
                        "number": "10",
                        "title": "Love Buzz",
                        "duration": "243840"
                    },
                    {
                        "number": "11",
                        "title": "Floyd the Barber",
                        "duration": "154293"
                    },
                    {
                        "number": "12",
                        "title": "Downer",
                        "duration": "146373"
                    },
                    {
                        "number": "13",
                        "title": "Pre-Mexican Seafood Noise",
                        "duration": "14666"
                    },
                    {
                        "number": "14",
                        "title": "Mexican Seafood",
                        "duration": "131453"
                    },
                    {
                        "number": "15",
                        "title": "White Lace and Strange",
                        "duration": "126960"
                    },
                    {
                        "number": "16",
                        "title": "Spank Thru / Anorexorcist",
                        "duration": "379600"
                    },
                    {
                        "number": "17",
                        "title": "Hairspray Queen",
                        "duration": "295480"
                    },
                    {
                        "number": "18",
                        "title": "Pen Cap Chew",
                        "duration": "271147"
                    }
                ]
            },
            {
                "id": "2251576",
                "title": "Wipeout",
                "year": "1993",
                "genre": "Grunge",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Spank Thru",
                        "duration": "182000"
                    },
                    {
                        "number": "2",
                        "title": "About a Girl",
                        "duration": "158000"
                    },
                    {
                        "number": "3",
                        "title": "Love Buzz",
                        "duration": "199000"
                    },
                    {
                        "number": "4",
                        "title": "Polly",
                        "duration": "157000"
                    },
                    {
                        "number": "5",
                        "title": "Son of a Gun",
                        "duration": "167000"
                    },
                    {
                        "number": "6",
                        "title": "Turnaround",
                        "duration": "140000"
                    },
                    {
                        "number": "7",
                        "title": "D-7",
                        "duration": "228000"
                    },
                    {
                        "number": "8",
                        "title": "Molly's Lips",
                        "duration": "109000"
                    },
                    {
                        "number": "9",
                        "title": "Sappy",
                        "duration": "204000"
                    },
                    {
                        "number": "10",
                        "title": "Lithium",
                        "duration": "249000"
                    },
                    {
                        "number": "11",
                        "title": "Breed",
                        "duration": "182000"
                    },
                    {
                        "number": "12",
                        "title": "In Bloom",
                        "duration": "264000"
                    },
                    {
                        "number": "13",
                        "title": "Stay Away",
                        "duration": "203000"
                    }
                ]
            },
            {
                "id": "2251577",
                "title": "Outcesticide III: The Final Solution",
                "year": "1995",
                "genre": "Grunge",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Rape Me (live - 4 Feb 94, French TV)",
                        "duration": "167346"
                    },
                    {
                        "number": "2",
                        "title": "Pennyroyal Tea (live - 4 Feb 94, French TV)",
                        "duration": "232040"
                    },
                    {
                        "number": "3",
                        "title": "Drain You (live - 4 Feb 94, French TV)",
                        "duration": "224053"
                    },
                    {
                        "number": "4",
                        "title": "Marigold (original demo)",
                        "duration": "185906"
                    },
                    {
                        "number": "5",
                        "title": "Dive (early version)",
                        "duration": "213800"
                    },
                    {
                        "number": "6",
                        "title": "Mr. Moustache (version)",
                        "duration": "216600"
                    },
                    {
                        "number": "7",
                        "title": "Blandest",
                        "duration": "230613"
                    },
                    {
                        "number": "8",
                        "title": "Even in His Youth (version)",
                        "duration": "190133"
                    },
                    {
                        "number": "9",
                        "title": "Polly (Outtake)",
                        "duration": "162866"
                    },
                    {
                        "number": "10",
                        "title": "Smells Like Teen Spirit (live - 10 Jan 92, Mt)",
                        "duration": "272000"
                    },
                    {
                        "number": "11",
                        "title": "Serve the Servants (live - 23 Feb 94, Italian TV)",
                        "duration": "202240"
                    },
                    {
                        "number": "12",
                        "title": "Dumb (live - 23 Feb 94, Italian TV)",
                        "duration": "154173"
                    },
                    {
                        "number": "13",
                        "title": "tourette's",
                        "duration": "126973"
                    },
                    {
                        "number": "14",
                        "title": "Aneurysm (Early Live Version - Nov 90)",
                        "duration": "281773"
                    },
                    {
                        "number": "15",
                        "title": "Oh, the Guilt (Early Live Version - Nov 90)",
                        "duration": "193946"
                    },
                    {
                        "number": "16",
                        "title": "Dive (VPRO Radio, The Netherlands)",
                        "duration": "244133"
                    },
                    {
                        "number": "17",
                        "title": "About a Girl (VPRO Radio, The Netherlands)",
                        "duration": "160506"
                    },
                    {
                        "number": "18",
                        "title": "The Money Will Roll Right In (live, 1992-08)",
                        "duration": "135413"
                    },
                    {
                        "number": "19",
                        "title": "Verse Chorus Verse",
                        "duration": "191106"
                    },
                    {
                        "number": "20",
                        "title": "Curmudgeon",
                        "duration": "168213"
                    },
                    {
                        "number": "21",
                        "title": "High on the Hog (live, 1989-10: Italy)",
                        "duration": "128066"
                    },
                    {
                        "number": "22",
                        "title": "Raunchola",
                        "duration": "241266"
                    },
                    {
                        "number": "23",
                        "title": "Beans",
                        "duration": "76827"
                    }
                ]
            },
            {
                "id": "2251582",
                "title": "Seventh Heaven",
                "year": "1992",
                "genre": "Grunge",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Drain You",
                        "duration": "237333"
                    },
                    {
                        "number": "2",
                        "title": "Aneurysm",
                        "duration": "266826"
                    },
                    {
                        "number": "3",
                        "title": "School",
                        "duration": "151173"
                    },
                    {
                        "number": "4",
                        "title": "Been A Son",
                        "duration": "125160"
                    },
                    {
                        "number": "5",
                        "title": "Negative Creep",
                        "duration": "163173"
                    },
                    {
                        "number": "6",
                        "title": "Smells Like Teen Spirit",
                        "duration": "281333"
                    },
                    {
                        "number": "7",
                        "title": "Aneurysm",
                        "duration": "298333"
                    },
                    {
                        "number": "8",
                        "title": "School",
                        "duration": "167826"
                    },
                    {
                        "number": "9",
                        "title": "Floyd the Barber",
                        "duration": "150173"
                    },
                    {
                        "number": "10",
                        "title": "Smells Like Teen Spirit",
                        "duration": "287666"
                    },
                    {
                        "number": "11",
                        "title": "About a Girl",
                        "duration": "182000"
                    },
                    {
                        "number": "12",
                        "title": "Polly",
                        "duration": "173333"
                    },
                    {
                        "number": "13",
                        "title": "Lithium",
                        "duration": "296333"
                    },
                    {
                        "number": "14",
                        "title": "Sliver",
                        "duration": "134666"
                    },
                    {
                        "number": "15",
                        "title": "Come as You Are",
                        "duration": "227093"
                    },
                    {
                        "number": "16",
                        "title": "Breed",
                        "duration": "200906"
                    },
                    {
                        "number": "17",
                        "title": "Been A Son",
                        "duration": "124493"
                    },
                    {
                        "number": "18",
                        "title": "Negative Creep",
                        "duration": "150173"
                    },
                    {
                        "number": "19",
                        "title": "On a Plain",
                        "duration": "206333"
                    },
                    {
                        "number": "20",
                        "title": "Blew",
                        "duration": "195160"
                    },
                    {
                        "number": "21",
                        "title": "Big Cheese",
                        "duration": "170840"
                    },
                    {
                        "number": "22",
                        "title": "Spank Thru",
                        "duration": "219333"
                    },
                    {
                        "number": "23",
                        "title": "Territorial Pissings",
                        "duration": "134894"
                    }
                ]
            },
            {
                "id": "2251586",
                "title": "The Eternal Legacy",
                "year": "1994",
                "genre": "Grunge",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Love Buzz",
                        "duration": "199000"
                    },
                    {
                        "number": "2",
                        "title": "About a Girl",
                        "duration": "160000"
                    },
                    {
                        "number": "3",
                        "title": "Polly",
                        "duration": "157000"
                    },
                    {
                        "number": "4",
                        "title": "Spank Thru",
                        "duration": "196000"
                    },
                    {
                        "number": "5",
                        "title": "Son of a Gun",
                        "duration": "166000"
                    },
                    {
                        "number": "6",
                        "title": "Molly's Lips",
                        "duration": "110000"
                    },
                    {
                        "number": "7",
                        "title": "D-7",
                        "duration": "224000"
                    },
                    {
                        "number": "8",
                        "title": "Turn Around",
                        "duration": "136000"
                    },
                    {
                        "number": "9",
                        "title": "Dumb",
                        "duration": "155000"
                    },
                    {
                        "number": "10",
                        "title": "Drain You",
                        "duration": "241000"
                    },
                    {
                        "number": "11",
                        "title": "Endless, Nameless",
                        "duration": "527000"
                    },
                    {
                        "number": "12",
                        "title": "Drain You",
                        "duration": "223000"
                    },
                    {
                        "number": "13",
                        "title": "Aneurysm",
                        "duration": "265000"
                    },
                    {
                        "number": "14",
                        "title": "School",
                        "duration": "159000"
                    },
                    {
                        "number": "15",
                        "title": "Floyd the Barber",
                        "duration": "141000"
                    },
                    {
                        "number": "16",
                        "title": "Smells Like Teen Spirit",
                        "duration": "292000"
                    },
                    {
                        "number": "17",
                        "title": "About a Girl",
                        "duration": "176000"
                    },
                    {
                        "number": "18",
                        "title": "Polly",
                        "duration": "176000"
                    },
                    {
                        "number": "19",
                        "title": "Sliver",
                        "duration": "123000"
                    },
                    {
                        "number": "20",
                        "title": "Breed",
                        "duration": "175000"
                    },
                    {
                        "number": "21",
                        "title": "Come as You Are",
                        "duration": "224000"
                    },
                    {
                        "number": "22",
                        "title": "Lithium",
                        "duration": "290000"
                    },
                    {
                        "number": "23",
                        "title": "Territorial Pissings",
                        "duration": "231000"
                    }
                ]
            },
            {
                "id": "2251605",
                "title": "Before We Ever Minded",
                "year": "1992",
                "genre": "Grunge",
                "tracks": [
                    {
                        "number": "1",
                        "title": "In Bloom (studio, 1990-04-02 to 1990-04-06: Smart Studios, Madison, WI, USA)",
                        "duration": "272533"
                    },
                    {
                        "number": "2",
                        "title": "Breed (studio, 1990-04-02 to 1990-04-06: Smart Studios, Madison, WI, USA)",
                        "duration": "193400"
                    },
                    {
                        "number": "3",
                        "title": "Stay Away",
                        "duration": "209360"
                    },
                    {
                        "number": "4",
                        "title": "Sappy (studio, 1990-04-02 to 1990-04-06: Smart Studios, Madison, WI, USA)",
                        "duration": "208933"
                    },
                    {
                        "number": "5",
                        "title": "Son of a Gun (studio, 1990-10-21: John Peel Sessions, BBC Radio 1, Maida Vale Studio 3, London, UK)",
                        "duration": "180333"
                    },
                    {
                        "number": "6",
                        "title": "Love Buzz (live, 1990-04-10: Blind Pig, Ann Arbor, MI, USA)",
                        "duration": "263466"
                    },
                    {
                        "number": "7",
                        "title": "Dive (live, 1990-04-10: Blind Pig, Ann Arbor, MI, USA)",
                        "duration": "214200"
                    },
                    {
                        "number": "8",
                        "title": "Love Buzz",
                        "duration": "200906"
                    },
                    {
                        "number": "9",
                        "title": "About a Girl",
                        "duration": "161133"
                    },
                    {
                        "number": "10",
                        "title": "Polly",
                        "duration": "160760"
                    },
                    {
                        "number": "11",
                        "title": "Spank Thru (studio, 1989-10-26: John Peel Sessions, BBC Radio 1, Maida Vale Studio 3, London, UK)",
                        "duration": "199506"
                    },
                    {
                        "number": "12",
                        "title": "If You Must (studio, 1988-01-23: Reciprocal Recording Studios, Seattle, WA, USA)",
                        "duration": "247800"
                    },
                    {
                        "number": "13",
                        "title": "Downer (studio, 1988-01-23: Reciprocal Recording Studios, Seattle, WA, USA)",
                        "duration": "103493"
                    },
                    {
                        "number": "14",
                        "title": "Hairspray Queen (studio, 1988-01-23: Reciprocal Recording Studios, Seattle, WA, USA)",
                        "duration": "247734"
                    }
                ]
            },
            {
                "id": "2251639",
                "title": "B-Side Themselves",
                "year": "1995",
                "genre": "Grunge",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Turnaround",
                        "duration": "139066"
                    },
                    {
                        "number": "2",
                        "title": "D-7",
                        "duration": "228453"
                    },
                    {
                        "number": "3",
                        "title": "Son of a Gun",
                        "duration": "167320"
                    },
                    {
                        "number": "4",
                        "title": "Molly's Lips",
                        "duration": "113386"
                    },
                    {
                        "number": "5",
                        "title": "Aneurysm",
                        "duration": "288520"
                    },
                    {
                        "number": "6",
                        "title": "Even in His Youth",
                        "duration": "186880"
                    },
                    {
                        "number": "7",
                        "title": "Been a Son",
                        "duration": "114760"
                    },
                    {
                        "number": "8",
                        "title": "(New Wave) Polly",
                        "duration": "108586"
                    },
                    {
                        "number": "9",
                        "title": "Something in the Way",
                        "duration": "188906"
                    },
                    {
                        "number": "10",
                        "title": "Here She Comes Now",
                        "duration": "300986"
                    },
                    {
                        "number": "11",
                        "title": "Curmudgeon",
                        "duration": "179626"
                    },
                    {
                        "number": "12",
                        "title": "Oh, the Guilt",
                        "duration": "204666"
                    },
                    {
                        "number": "13",
                        "title": "Return of the Rat",
                        "duration": "189373"
                    },
                    {
                        "number": "14",
                        "title": "Endless, Nameless",
                        "duration": "405626"
                    },
                    {
                        "number": "15",
                        "title": "Pay to Play (demo, 1990)",
                        "duration": "209933"
                    },
                    {
                        "number": "16",
                        "title": "I Hate Myself and Want to Die",
                        "duration": "165560"
                    },
                    {
                        "number": "17",
                        "title": "Sappy",
                        "duration": "205893"
                    },
                    {
                        "number": "18",
                        "title": "Marigold",
                        "duration": "156600"
                    },
                    {
                        "number": "19",
                        "title": "Moist Vagina",
                        "duration": "215666"
                    },
                    {
                        "number": "20",
                        "title": "Gallons of Rubbing Alchohol Flow Through the Strip",
                        "duration": "453946"
                    }
                ]
            },
            {
                "id": "2270453",
                "title": "Nevermind, It's An Interview",
                "year": "1992",
                "genre": "Grunge",
                "tracks": [
                    {
                        "number": "1",
                        "title": "[interview, part 1]",
                        "duration": "1064000"
                    },
                    {
                        "number": "2",
                        "title": "[interview, part 2]",
                        "duration": "1094000"
                    },
                    {
                        "number": "3",
                        "title": "[interview, part 3]",
                        "duration": "1067000"
                    }
                ]
            }
        ]
    },
    "Imagine Dragons": {
        "albums": [
            {
                "id": "2131099",
                "title": "Night Visions",
                "year": "2012",
                "genre": "Indie",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Radioactive",
                        "duration": "186813"
                    },
                    {
                        "number": "2",
                        "title": "Tiptoe",
                        "duration": "194200"
                    },
                    {
                        "number": "3",
                        "title": "It's Time",
                        "duration": "240306"
                    },
                    {
                        "number": "4",
                        "title": "Demons",
                        "duration": "177506"
                    },
                    {
                        "number": "5",
                        "title": "On Top of the World",
                        "duration": "192280"
                    },
                    {
                        "number": "6",
                        "title": "Amsterdam",
                        "duration": "241426"
                    },
                    {
                        "number": "7",
                        "title": "Hear Me",
                        "duration": "235386"
                    },
                    {
                        "number": "8",
                        "title": "Every Night",
                        "duration": "217346"
                    },
                    {
                        "number": "9",
                        "title": "Bleeding Out",
                        "duration": "223106"
                    },
                    {
                        "number": "10",
                        "title": "Underdog",
                        "duration": "209440"
                    },
                    {
                        "number": "11",
                        "title": "Nothing Left to Say / Rocks",
                        "duration": "536080"
                    },
                    {
                        "number": "12",
                        "title": "Selene",
                        "duration": "242000"
                    },
                    {
                        "number": "13",
                        "title": "The River",
                        "duration": "204000"
                    }
                ]
            },
            {
                "id": "2215914",
                "title": "Battle Cry",
                "year": "2014",
                "genre": "Indie",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Battle Cry",
                        "duration": "273000"
                    }
                ]
            },
            {
                "id": "2225780",
                "title": "I Bet My Life",
                "year": "2014",
                "genre": "Indie",
                "tracks": [
                    {
                        "number": "1",
                        "title": "I Bet My Life",
                        "duration": "192000"
                    }
                ]
            },
            {
                "id": "2225934",
                "title": "Smoke + Mirrors",
                "year": "2015",
                "genre": "Indie",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Shots",
                        "duration": "232000"
                    },
                    {
                        "number": "2",
                        "title": "Gold",
                        "duration": "216000"
                    },
                    {
                        "number": "3",
                        "title": "Smoke and Mirrors",
                        "duration": "260000"
                    },
                    {
                        "number": "4",
                        "title": "I'm So Sorry",
                        "duration": "230000"
                    },
                    {
                        "number": "5",
                        "title": "I Bet My Life",
                        "duration": "192000"
                    },
                    {
                        "number": "6",
                        "title": "Polaroid",
                        "duration": "231000"
                    },
                    {
                        "number": "7",
                        "title": "Friction",
                        "duration": "201000"
                    },
                    {
                        "number": "8",
                        "title": "It Comes Back to You",
                        "duration": "217000"
                    },
                    {
                        "number": "9",
                        "title": "Dream",
                        "duration": "258000"
                    },
                    {
                        "number": "10",
                        "title": "Trouble",
                        "duration": "192000"
                    },
                    {
                        "number": "11",
                        "title": "Summer",
                        "duration": "218000"
                    },
                    {
                        "number": "12",
                        "title": "Hopeless Opus",
                        "duration": "241000"
                    },
                    {
                        "number": "13",
                        "title": "The Fall",
                        "duration": "365000"
                    },
                    {
                        "number": "14",
                        "title": "Thief",
                        "duration": "227000"
                    },
                    {
                        "number": "15",
                        "title": "The Unknown",
                        "duration": "204000"
                    },
                    {
                        "number": "16",
                        "title": "Second Chances",
                        "duration": "217000"
                    },
                    {
                        "number": "17",
                        "title": "Release",
                        "duration": "148000"
                    },
                    {
                        "number": "18",
                        "title": "Warriors",
                        "duration": "170000"
                    }
                ]
            },
            {
                "id": "2250225",
                "title": "Roots",
                "year": "2015",
                "genre": "Indie",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Roots",
                        "duration": "174493"
                    }
                ]
            },
            {
                "id": "2281777",
                "title": "Evolve",
                "year": "2017",
                "genre": "Indie",
                "tracks": [
                    {
                        "number": "1",
                        "title": "I Don't Know Why",
                        "duration": "190131"
                    },
                    {
                        "number": "2",
                        "title": "Whatever It Takes",
                        "duration": "201241"
                    },
                    {
                        "number": "3",
                        "title": "Believer",
                        "duration": "204345"
                    },
                    {
                        "number": "4",
                        "title": "Walking the Wire",
                        "duration": "232909"
                    },
                    {
                        "number": "5",
                        "title": "Rise Up",
                        "duration": "231712"
                    },
                    {
                        "number": "6",
                        "title": "I'll Make It Up to You",
                        "duration": "262602"
                    },
                    {
                        "number": "7",
                        "title": "Yesterday",
                        "duration": "205114"
                    },
                    {
                        "number": "8",
                        "title": "Mouth of the River",
                        "duration": "221563"
                    },
                    {
                        "number": "9",
                        "title": "Thunder",
                        "duration": "187145"
                    },
                    {
                        "number": "10",
                        "title": "Start Over",
                        "duration": "186089"
                    },
                    {
                        "number": "11",
                        "title": "Dancing in the Dark",
                        "duration": "233923"
                    },
                    {
                        "number": "12",
                        "title": "Levitate",
                        "duration": "198000"
                    },
                    {
                        "number": "13",
                        "title": "Not Today",
                        "duration": "261000"
                    },
                    {
                        "number": "14",
                        "title": "Believer (Kaskade remix)",
                        "duration": "191000"
                    }
                ]
            },
            {
                "id": "2296266",
                "title": "On Top of the World",
                "year": "2013",
                "genre": "Indie",
                "tracks": [
                    {
                        "number": "1",
                        "title": "On Top of the World",
                        "duration": "189000"
                    }
                ]
            },
            {
                "id": "2306531",
                "title": "Natural",
                "year": "2018",
                "genre": "",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Natural",
                        "duration": "189467"
                    }
                ]
            },
            {
                "id": "2308836",
                "title": "Origins",
                "year": "2018",
                "genre": "Indie",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Natural",
                        "duration": "189467"
                    },
                    {
                        "number": "2",
                        "title": "Boomerang",
                        "duration": "188000"
                    },
                    {
                        "number": "3",
                        "title": "Machine",
                        "duration": "182000"
                    },
                    {
                        "number": "4",
                        "title": "Cool Out",
                        "duration": "218000"
                    },
                    {
                        "number": "5",
                        "title": "Bad Liar",
                        "duration": "261000"
                    },
                    {
                        "number": "6",
                        "title": "West Coast",
                        "duration": "217000"
                    },
                    {
                        "number": "7",
                        "title": "Zero (from the original motion picture \u201cRalph Breaks the Internet\u201d)",
                        "duration": "210935"
                    },
                    {
                        "number": "8",
                        "title": "Bullet in a Gun",
                        "duration": "205000"
                    },
                    {
                        "number": "9",
                        "title": "Digital",
                        "duration": "201000"
                    },
                    {
                        "number": "10",
                        "title": "Only",
                        "duration": "181000"
                    },
                    {
                        "number": "11",
                        "title": "Stuck",
                        "duration": "191000"
                    },
                    {
                        "number": "12",
                        "title": "Love",
                        "duration": "166000"
                    }
                ]
            },
            {
                "id": "2309504",
                "title": "Night Visions Live",
                "year": "2014",
                "genre": "",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Radioactive",
                        "duration": "403693"
                    },
                    {
                        "number": "2",
                        "title": "Hear Me",
                        "duration": "293520"
                    },
                    {
                        "number": "3",
                        "title": "On Top of the World",
                        "duration": "201453"
                    },
                    {
                        "number": "4",
                        "title": "Round and Round",
                        "duration": "218013"
                    },
                    {
                        "number": "5",
                        "title": "Amsterdam",
                        "duration": "250493"
                    },
                    {
                        "number": "6",
                        "title": "Tip Toe",
                        "duration": "334853"
                    },
                    {
                        "number": "7",
                        "title": "Cha-Ching",
                        "duration": "282760"
                    },
                    {
                        "number": "8",
                        "title": "Rocks",
                        "duration": "223346"
                    },
                    {
                        "number": "9",
                        "title": "Demons",
                        "duration": "196160"
                    },
                    {
                        "number": "10",
                        "title": "Underdog",
                        "duration": "257600"
                    },
                    {
                        "number": "11",
                        "title": "It's Time",
                        "duration": "329440"
                    },
                    {
                        "number": "12",
                        "title": "It's Time (acoustic)",
                        "duration": "250226"
                    },
                    {
                        "number": "13",
                        "title": "Radioactive (acoustic)",
                        "duration": "270400"
                    },
                    {
                        "number": "14",
                        "title": "Demons (acoustic)",
                        "duration": "187426"
                    }
                ]
            },
            {
                "id": "2309505",
                "title": "Greatest Hits",
                "year": "2017",
                "genre": "",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Believer",
                        "duration": "204000"
                    },
                    {
                        "number": "2",
                        "title": "Walking the Wire",
                        "duration": "233000"
                    },
                    {
                        "number": "3",
                        "title": "Whatever It Takes",
                        "duration": "201000"
                    },
                    {
                        "number": "4",
                        "title": "Thunder",
                        "duration": "187000"
                    },
                    {
                        "number": "5",
                        "title": "Levitate",
                        "duration": "198000"
                    },
                    {
                        "number": "6",
                        "title": "Sucker for Pain",
                        "duration": "244000"
                    },
                    {
                        "number": "7",
                        "title": "Roots",
                        "duration": "174000"
                    },
                    {
                        "number": "8",
                        "title": "I Bet My Life",
                        "duration": "194000"
                    },
                    {
                        "number": "9",
                        "title": "Shots",
                        "duration": "232000"
                    },
                    {
                        "number": "10",
                        "title": "Gold",
                        "duration": "216000"
                    },
                    {
                        "number": "11",
                        "title": "Dream",
                        "duration": "258000"
                    },
                    {
                        "number": "12",
                        "title": "Warriors",
                        "duration": "170000"
                    },
                    {
                        "number": "13",
                        "title": "Monster",
                        "duration": "251000"
                    },
                    {
                        "number": "14",
                        "title": "Battle Cry",
                        "duration": "274000"
                    },
                    {
                        "number": "15",
                        "title": "Who We Are",
                        "duration": "249000"
                    },
                    {
                        "number": "16",
                        "title": "Radioactive",
                        "duration": "187000"
                    },
                    {
                        "number": "17",
                        "title": "It\u2019s Time",
                        "duration": "240000"
                    },
                    {
                        "number": "18",
                        "title": "Demons",
                        "duration": "176000"
                    },
                    {
                        "number": "19",
                        "title": "On Top of the World",
                        "duration": "192000"
                    },
                    {
                        "number": "20",
                        "title": "Bleeding Out",
                        "duration": "223000"
                    },
                    {
                        "number": "21",
                        "title": "Round and Round",
                        "duration": "198000"
                    },
                    {
                        "number": "22",
                        "title": "Uptight",
                        "duration": "224000"
                    },
                    {
                        "number": "1",
                        "title": "I Don\u2019t Know Why",
                        "duration": "190000"
                    },
                    {
                        "number": "2",
                        "title": "I\u2019ll Make It Up to You",
                        "duration": "263000"
                    },
                    {
                        "number": "3",
                        "title": "Mouth of the River",
                        "duration": "222000"
                    },
                    {
                        "number": "4",
                        "title": "Not Today",
                        "duration": "261000"
                    },
                    {
                        "number": "5",
                        "title": "I\u2019m So Sorry",
                        "duration": "230000"
                    },
                    {
                        "number": "6",
                        "title": "Friction",
                        "duration": "201000"
                    },
                    {
                        "number": "7",
                        "title": "Thief",
                        "duration": "227000"
                    },
                    {
                        "number": "8",
                        "title": "Smoke and Mirrors",
                        "duration": "260000"
                    },
                    {
                        "number": "9",
                        "title": "Polaroid",
                        "duration": "231000"
                    },
                    {
                        "number": "10",
                        "title": "It Comes Back to You",
                        "duration": "217000"
                    },
                    {
                        "number": "11",
                        "title": "Tiptoe",
                        "duration": "194000"
                    },
                    {
                        "number": "12",
                        "title": "Amsterdam",
                        "duration": "181000"
                    },
                    {
                        "number": "13",
                        "title": "Hear Me",
                        "duration": "235000"
                    },
                    {
                        "number": "14",
                        "title": "Working Man",
                        "duration": "235000"
                    },
                    {
                        "number": "15",
                        "title": "The River",
                        "duration": "204000"
                    },
                    {
                        "number": "16",
                        "title": "America",
                        "duration": "273000"
                    },
                    {
                        "number": "17",
                        "title": "Selene",
                        "duration": "240000"
                    },
                    {
                        "number": "18",
                        "title": "Tokyo",
                        "duration": "195000"
                    },
                    {
                        "number": "19",
                        "title": "Leave Me",
                        "duration": "211000"
                    },
                    {
                        "number": "20",
                        "title": "All Eyes",
                        "duration": "179000"
                    },
                    {
                        "number": "21",
                        "title": "I Don\u2019t Mind",
                        "duration": "198000"
                    }
                ]
            },
            {
                "id": "2309506",
                "title": "Imagine Dragons",
                "year": "2017",
                "genre": "",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Radioactive",
                        "duration": "188000"
                    },
                    {
                        "number": "2",
                        "title": "Demons",
                        "duration": "176000"
                    },
                    {
                        "number": "3",
                        "title": "On Top of the World",
                        "duration": "191000"
                    },
                    {
                        "number": "4",
                        "title": "Round and Round",
                        "duration": "198000"
                    },
                    {
                        "number": "5",
                        "title": "It\u2019s Time",
                        "duration": "240000"
                    },
                    {
                        "number": "6",
                        "title": "My Fault",
                        "duration": "175000"
                    },
                    {
                        "number": "1",
                        "title": "Radioactive",
                        "duration": "186813"
                    },
                    {
                        "number": "2",
                        "title": "Tiptoe",
                        "duration": "194200"
                    },
                    {
                        "number": "3",
                        "title": "It\u2019s Time",
                        "duration": "240306"
                    },
                    {
                        "number": "4",
                        "title": "Demons",
                        "duration": "177506"
                    },
                    {
                        "number": "5",
                        "title": "On Top of the World",
                        "duration": "192280"
                    },
                    {
                        "number": "6",
                        "title": "Amsterdam",
                        "duration": "241426"
                    },
                    {
                        "number": "7",
                        "title": "Hear Me",
                        "duration": "235386"
                    },
                    {
                        "number": "8",
                        "title": "Every Night",
                        "duration": "217346"
                    },
                    {
                        "number": "9",
                        "title": "Bleeding Out",
                        "duration": "223106"
                    },
                    {
                        "number": "10",
                        "title": "Underdog",
                        "duration": "209440"
                    },
                    {
                        "number": "11",
                        "title": "Nothing Left to Say / Rocks",
                        "duration": "536080"
                    },
                    {
                        "number": "1",
                        "title": "Shots",
                        "duration": "232000"
                    },
                    {
                        "number": "2",
                        "title": "Gold",
                        "duration": "217000"
                    },
                    {
                        "number": "3",
                        "title": "Smoke and Mirrors",
                        "duration": "261000"
                    },
                    {
                        "number": "4",
                        "title": "I\u2019m So Sorry",
                        "duration": "230000"
                    },
                    {
                        "number": "5",
                        "title": "I Bet My Life",
                        "duration": "194000"
                    },
                    {
                        "number": "6",
                        "title": "Polaroid",
                        "duration": "231000"
                    },
                    {
                        "number": "7",
                        "title": "Friction",
                        "duration": "202000"
                    },
                    {
                        "number": "8",
                        "title": "It Comes Back to You",
                        "duration": "217000"
                    },
                    {
                        "number": "9",
                        "title": "Dream",
                        "duration": "259000"
                    },
                    {
                        "number": "10",
                        "title": "Trouble",
                        "duration": "193000"
                    },
                    {
                        "number": "1",
                        "title": "Summer",
                        "duration": "218000"
                    },
                    {
                        "number": "2",
                        "title": "Hopeless Opus",
                        "duration": "242000"
                    },
                    {
                        "number": "3",
                        "title": "The Fall",
                        "duration": "362000"
                    },
                    {
                        "number": "4",
                        "title": "Thief",
                        "duration": "228000"
                    },
                    {
                        "number": "5",
                        "title": "The Unknown",
                        "duration": "205000"
                    },
                    {
                        "number": "6",
                        "title": "Second Chances",
                        "duration": "218000"
                    },
                    {
                        "number": "7",
                        "title": "Release",
                        "duration": "149000"
                    },
                    {
                        "number": "8",
                        "title": "Warriors",
                        "duration": "171000"
                    },
                    {
                        "number": "9",
                        "title": "Battle Cry",
                        "duration": "272000"
                    },
                    {
                        "number": "10",
                        "title": "Monster",
                        "duration": "249000"
                    },
                    {
                        "number": "11",
                        "title": "Who We Are",
                        "duration": "249000"
                    },
                    {
                        "number": "1",
                        "title": "I Don\u2019t Know Why",
                        "duration": "190131"
                    },
                    {
                        "number": "2",
                        "title": "Whatever It Takes",
                        "duration": "201241"
                    },
                    {
                        "number": "3",
                        "title": "Believer",
                        "duration": "204345"
                    },
                    {
                        "number": "4",
                        "title": "Walking the Wire",
                        "duration": "232909"
                    },
                    {
                        "number": "5",
                        "title": "Rise Up",
                        "duration": "231712"
                    },
                    {
                        "number": "6",
                        "title": "I\u2019ll Make It Up to You",
                        "duration": "262602"
                    },
                    {
                        "number": "7",
                        "title": "Yesterday",
                        "duration": "205114"
                    },
                    {
                        "number": "8",
                        "title": "Mouth of the River",
                        "duration": "221563"
                    },
                    {
                        "number": "9",
                        "title": "Thunder",
                        "duration": "187145"
                    },
                    {
                        "number": "10",
                        "title": "Start Over",
                        "duration": "186089"
                    },
                    {
                        "number": "11",
                        "title": "Dancing in the Dark",
                        "duration": "233923"
                    }
                ]
            },
            {
                "id": "2324306",
                "title": "Bad Liar",
                "year": "2018",
                "genre": "Indie",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Bad Liar",
                        "duration": "260000"
                    }
                ]
            },
            {
                "id": "2336880",
                "title": "Hitlist The Greatest Of Imagine Dragons",
                "year": "2018",
                "genre": '',
                "tracks": [
                    {
                        "number": "1",
                        "title": "On Top Of The World",
                        "duration": "192000"
                    },
                    {
                        "number": "2",
                        "title": "Machine",
                        "duration": "182000"
                    },
                    {
                        "number": "3",
                        "title": "Whatever It Takes",
                        "duration": "201000"
                    },
                    {
                        "number": "4",
                        "title": "Battle Cry",
                        "duration": "274000"
                    },
                    {
                        "number": "5",
                        "title": "It's Time",
                        "duration": "240000"
                    },
                    {
                        "number": "6",
                        "title": "Next To Me",
                        "duration": "231000"
                    },
                    {
                        "number": "7",
                        "title": "Not Today",
                        "duration": "261000"
                    },
                    {
                        "number": "8",
                        "title": "Radioactive",
                        "duration": "187000"
                    },
                    {
                        "number": "9",
                        "title": "Warriors",
                        "duration": "171000"
                    },
                    {
                        "number": "10",
                        "title": "I Bet My Life",
                        "duration": "194000"
                    },
                    {
                        "number": "11",
                        "title": "Gold",
                        "duration": "217000"
                    },
                    {
                        "number": "12",
                        "title": "Shots",
                        "duration": "232000"
                    },
                    {
                        "number": "13",
                        "title": "Natural",
                        "duration": "190000"
                    },
                    {
                        "number": "14",
                        "title": "Monster",
                        "duration": "251000"
                    },
                    {
                        "number": "15",
                        "title": "Zero",
                        "duration": "211000"
                    },
                    {
                        "number": "16",
                        "title": "Walking The Wire",
                        "duration": "233000"
                    },
                    {
                        "number": "17",
                        "title": "Demons",
                        "duration": "178000"
                    },
                    {
                        "number": "18",
                        "title": "Believer",
                        "duration": "204000"
                    },
                    {
                        "number": "19",
                        "title": "Thunder",
                        "duration": "187000"
                    },
                    {
                        "number": "20",
                        "title": "Bleeding Out",
                        "duration": "223000"
                    },
                    {
                        "number": "21",
                        "title": "Bad Liar",
                        "duration": "261000"
                    },
                    {
                        "number": "22",
                        "title": "Dancing In The Dark",
                        "duration": "234000"
                    }
                ]
            },
            {
                "id": "2336881",
                "title": "Whatever It Takes",
                "year": "2017",
                "genre": '',
                "tracks": [
                    {
                        "number": "1",
                        "title": "Whatever It Takes",
                        "duration": "202000"
                    },
                    {
                        "number": "2",
                        "title": "Thunder (Official remix)",
                        "duration": "197000"
                    }
                ]
            },
            {
                "id": "2336882",
                "title": "Smoke + Mirrors Live",
                "year": "2015",
                "genre": '',
                "tracks": [
                    {
                        "number": "1",
                        "title": "Intro",
                        "duration": "126520"
                    },
                    {
                        "number": "2",
                        "title": "Shots",
                        "duration": "280440"
                    },
                    {
                        "number": "3",
                        "title": "It's Time",
                        "duration": "353906"
                    },
                    {
                        "number": "4",
                        "title": "Forever Young / Smoke and Mirrors (medley)",
                        "duration": "503386"
                    },
                    {
                        "number": "5",
                        "title": "Polaroid",
                        "duration": "305733"
                    },
                    {
                        "number": "6",
                        "title": "I'm So Sorry",
                        "duration": "307586"
                    },
                    {
                        "number": "7",
                        "title": "Gold",
                        "duration": "275626"
                    },
                    {
                        "number": "8",
                        "title": "Demons (feat. Bleeding Out and Warriors)",
                        "duration": "293813"
                    },
                    {
                        "number": "9",
                        "title": "On Top of the World",
                        "duration": "291800"
                    },
                    {
                        "number": "10",
                        "title": "Friction",
                        "duration": "265986"
                    },
                    {
                        "number": "11",
                        "title": "I Bet My Life",
                        "duration": "220186"
                    },
                    {
                        "number": "12",
                        "title": "Radioactive",
                        "duration": "461106"
                    },
                    {
                        "number": "13",
                        "title": "The Fall",
                        "duration": "345826"
                    }
                ]
            },
            {
                "id": "2336883",
                "title": "Round and Round",
                "year": "2010",
                "genre": '',
                "tracks": [
                    {
                        "number": "1",
                        "title": "Round and Round",
                        "duration": "197000"
                    }
                ]
            }
        ]
    },

    "Taylor Swift": {
        "albums": [
            {
                "id": "2111259",
                "title": "Taylor Swift",
                "year": "2006",
                "genre": "Country",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Tim McGraw",
                        "duration": "235000"
                    },
                    {
                        "number": "2",
                        "title": "Picture to Burn",
                        "duration": "175000"
                    },
                    {
                        "number": "3",
                        "title": "Teardrops on My Guitar",
                        "duration": "204000"
                    },
                    {
                        "number": "4",
                        "title": "A Place in This World",
                        "duration": "202000"
                    },
                    {
                        "number": "5",
                        "title": "Cold as You",
                        "duration": "241000"
                    },
                    {
                        "number": "6",
                        "title": "The Outside",
                        "duration": "209000"
                    },
                    {
                        "number": "7",
                        "title": "Tied Together With a Smile",
                        "duration": "251000"
                    },
                    {
                        "number": "8",
                        "title": "Stay Beautiful",
                        "duration": "238000"
                    },
                    {
                        "number": "9",
                        "title": "Should've Said No",
                        "duration": "244000"
                    },
                    {
                        "number": "10",
                        "title": "Mary's Song (Oh My My My)",
                        "duration": "215000"
                    },
                    {
                        "number": "11",
                        "title": "Our Song",
                        "duration": "203000"
                    },
                    {
                        "number": "12",
                        "title": "I'm Only Me When I'm With You",
                        "duration": "215000"
                    },
                    {
                        "number": "13",
                        "title": "Invisible",
                        "duration": "205000"
                    },
                    {
                        "number": "14",
                        "title": "A Perfectly Good Heart",
                        "duration": "222000"
                    },
                    {
                        "number": "15",
                        "title": "Taylor's 1st Phone Call With Tim McGraw",
                        "duration": "283000"
                    }
                ]
            },
            {
                "id": "2116560",
                "title": "Fearless",
                "year": "2008",
                "genre": "Country",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Fearless",
                        "duration": "243000"
                    },
                    {
                        "number": "2",
                        "title": "Fifteen",
                        "duration": "295000"
                    },
                    {
                        "number": "3",
                        "title": "Love Story",
                        "duration": "236000"
                    },
                    {
                        "number": "4",
                        "title": "Hey Stephen",
                        "duration": "256000"
                    },
                    {
                        "number": "5",
                        "title": "White Horse",
                        "duration": "235000"
                    },
                    {
                        "number": "6",
                        "title": "You Belong With Me",
                        "duration": "232000"
                    },
                    {
                        "number": "7",
                        "title": "Breathe",
                        "duration": "265000"
                    },
                    {
                        "number": "8",
                        "title": "Tell Me Why",
                        "duration": "201000"
                    },
                    {
                        "number": "9",
                        "title": "You're Not Sorry",
                        "duration": "263000"
                    },
                    {
                        "number": "10",
                        "title": "The Way I Loved You",
                        "duration": "245000"
                    },
                    {
                        "number": "11",
                        "title": "Forever & Always",
                        "duration": "226000"
                    },
                    {
                        "number": "12",
                        "title": "The Best Day",
                        "duration": "246000"
                    },
                    {
                        "number": "13",
                        "title": "Change",
                        "duration": "280000"
                    }
                ]
            },
            {
                "id": "2125627",
                "title": "Red",
                "year": "2012",
                "genre": "Country",
                "tracks": [
                    {
                        "number": "1",
                        "title": "State of Grace",
                        "duration": "295000"
                    },
                    {
                        "number": "2",
                        "title": "Red",
                        "duration": "223000"
                    },
                    {
                        "number": "3",
                        "title": "Treacherous",
                        "duration": "243000"
                    },
                    {
                        "number": "4",
                        "title": "I Knew You Were Trouble",
                        "duration": "219000"
                    },
                    {
                        "number": "5",
                        "title": "All Too Well",
                        "duration": "329000"
                    },
                    {
                        "number": "6",
                        "title": "22",
                        "duration": "232000"
                    },
                    {
                        "number": "7",
                        "title": "I Almost Do",
                        "duration": "245000"
                    },
                    {
                        "number": "8",
                        "title": "We Are Never Ever Getting Back Together",
                        "duration": "191000"
                    },
                    {
                        "number": "9",
                        "title": "Stay Stay Stay",
                        "duration": "206000"
                    },
                    {
                        "number": "10",
                        "title": "The Last Time",
                        "duration": "299000"
                    },
                    {
                        "number": "11",
                        "title": "Holy Ground",
                        "duration": "203000"
                    },
                    {
                        "number": "12",
                        "title": "Sad Beautiful Tragic",
                        "duration": "285000"
                    },
                    {
                        "number": "13",
                        "title": "The Lucky One",
                        "duration": "240000"
                    },
                    {
                        "number": "14",
                        "title": "Everything Has Changed",
                        "duration": "245000"
                    },
                    {
                        "number": "15",
                        "title": "Starlight",
                        "duration": "221000"
                    },
                    {
                        "number": "16",
                        "title": "Begin Again",
                        "duration": "237000"
                    },
                    {
                        "number": "1",
                        "title": "The Moment I Knew",
                        "duration": "0"
                    },
                    {
                        "number": "2",
                        "title": "Come Back... Be Here",
                        "duration": "0"
                    },
                    {
                        "number": "3",
                        "title": "Girl at Home",
                        "duration": "0"
                    },
                    {
                        "number": "4",
                        "title": "Treacherous (original demo recording)",
                        "duration": "0"
                    },
                    {
                        "number": "5",
                        "title": "Red (original demo recording)",
                        "duration": "0"
                    },
                    {
                        "number": "6",
                        "title": "State of Grace (acoustic version)",
                        "duration": "0"
                    }
                ]
            },
            {
                "id": "2132504",
                "title": "Speak Now",
                "year": "2010",
                "genre": "Country",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Mine (pop mix)",
                        "duration": "232000"
                    },
                    {
                        "number": "2",
                        "title": "Sparks Fly",
                        "duration": "263000"
                    },
                    {
                        "number": "3",
                        "title": "Back to December",
                        "duration": "295000"
                    },
                    {
                        "number": "4",
                        "title": "Speak Now",
                        "duration": "243000"
                    },
                    {
                        "number": "5",
                        "title": "Dear John",
                        "duration": "406000"
                    },
                    {
                        "number": "6",
                        "title": "Mean",
                        "duration": "239000"
                    },
                    {
                        "number": "7",
                        "title": "The Story of Us",
                        "duration": "268000"
                    },
                    {
                        "number": "8",
                        "title": "Never Grow Up",
                        "duration": "293000"
                    },
                    {
                        "number": "9",
                        "title": "Enchanted",
                        "duration": "353000"
                    },
                    {
                        "number": "10",
                        "title": "Better Than Revenge",
                        "duration": "220000"
                    },
                    {
                        "number": "11",
                        "title": "Innocent",
                        "duration": "303000"
                    },
                    {
                        "number": "12",
                        "title": "Haunted",
                        "duration": "245000"
                    },
                    {
                        "number": "13",
                        "title": "Last Kiss",
                        "duration": "369000"
                    },
                    {
                        "number": "14",
                        "title": "Long Live",
                        "duration": "318000"
                    },
                    {
                        "number": "1",
                        "title": "Ours",
                        "duration": "239346"
                    },
                    {
                        "number": "2",
                        "title": "If This Was a Movie",
                        "duration": "236106"
                    },
                    {
                        "number": "3",
                        "title": "Superman",
                        "duration": "277520"
                    },
                    {
                        "number": "4",
                        "title": "Back to December (acoustic)",
                        "duration": "293946"
                    },
                    {
                        "number": "5",
                        "title": "Haunted (acoustic)",
                        "duration": "218946"
                    },
                    {
                        "number": "6",
                        "title": "Mine",
                        "duration": "232453"
                    },
                    {
                        "number": "7",
                        "title": "Back to December",
                        "duration": "294853"
                    },
                    {
                        "number": "8",
                        "title": "The Story of Us (US version)",
                        "duration": "265826"
                    }
                ]
            },
            {
                "id": "2161377",
                "title": "CMT Crossroads",
                "year": "2009",
                "genre": "Country",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Photograph",
                        "duration": "380000"
                    },
                    {
                        "number": "2",
                        "title": "Picture to Burn",
                        "duration": "277000"
                    },
                    {
                        "number": "3",
                        "title": "Love Story",
                        "duration": "361000"
                    },
                    {
                        "number": "4",
                        "title": "Hysteria",
                        "duration": "490000"
                    },
                    {
                        "number": "5",
                        "title": "Teardrops on My Guitar",
                        "duration": "280000"
                    },
                    {
                        "number": "6",
                        "title": "When Love and Hate Collide",
                        "duration": "235000"
                    },
                    {
                        "number": "7",
                        "title": "Should've Said No",
                        "duration": "241000"
                    },
                    {
                        "number": "8",
                        "title": "Pour Some Sugar on Me",
                        "duration": "335000"
                    },
                    {
                        "number": "9",
                        "title": "Our Song",
                        "duration": "240000"
                    },
                    {
                        "number": "10",
                        "title": "Love",
                        "duration": "266000"
                    },
                    {
                        "number": "11",
                        "title": "Two Steps Behind",
                        "duration": "299000"
                    }
                ]
            },
            {
                "id": "2222841",
                "title": "1989",
                "year": "2014",
                "genre": "Country",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Welcome to New York",
                        "duration": "212000"
                    },
                    {
                        "number": "2",
                        "title": "Blank Space",
                        "duration": "232000"
                    },
                    {
                        "number": "3",
                        "title": "Style",
                        "duration": "231000"
                    },
                    {
                        "number": "4",
                        "title": "Out of the Woods",
                        "duration": "235000"
                    },
                    {
                        "number": "5",
                        "title": "All You Had to Do Was Stay",
                        "duration": "193000"
                    },
                    {
                        "number": "6",
                        "title": "Shake It Off",
                        "duration": "219000"
                    },
                    {
                        "number": "7",
                        "title": "I Wish You Would",
                        "duration": "207000"
                    },
                    {
                        "number": "8",
                        "title": "Bad Blood",
                        "duration": "212000"
                    },
                    {
                        "number": "9",
                        "title": "Wildest Dreams",
                        "duration": "220000"
                    },
                    {
                        "number": "10",
                        "title": "How You Get the Girl",
                        "duration": "248000"
                    },
                    {
                        "number": "11",
                        "title": "This Love",
                        "duration": "250000"
                    },
                    {
                        "number": "12",
                        "title": "I Know Places",
                        "duration": "196000"
                    },
                    {
                        "number": "13",
                        "title": "Clean",
                        "duration": "271000"
                    },
                    {
                        "number": "14",
                        "title": "Wonderland",
                        "duration": "246000"
                    },
                    {
                        "number": "15",
                        "title": "You Are in Love",
                        "duration": "267000"
                    },
                    {
                        "number": "16",
                        "title": "New Romantics",
                        "duration": "230000"
                    },
                    {
                        "number": "17",
                        "title": "Out of the Woods (Voice Memo)",
                        "duration": "216000"
                    },
                    {
                        "number": "18",
                        "title": "Shake It Off (Voice Memo)",
                        "duration": "107000"
                    },
                    {
                        "number": "19",
                        "title": "I Know Places (Voice Memo)",
                        "duration": "131000"
                    }
                ]
            },
            {
                "id": "2251613",
                "title": "Everything Has Changed",
                "year": "2013",
                "genre": "",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Everything Has Changed",
                        "duration": "251000"
                    }
                ]
            },
            {
                "id": "2262136",
                "title": "The 1989 World Tour",
                "year": "2015",
                "genre": "Pop",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Welcome to New York",
                        "duration": "212000"
                    },
                    {
                        "number": "2",
                        "title": "New Romantics",
                        "duration": "230000"
                    },
                    {
                        "number": "3",
                        "title": "Blank Space",
                        "duration": "231826"
                    },
                    {
                        "number": "4",
                        "title": "I Knew You Were Trouble",
                        "duration": "630000"
                    },
                    {
                        "number": "5",
                        "title": "I Wish You Would",
                        "duration": "207000"
                    },
                    {
                        "number": "6",
                        "title": "How You Get the Girl",
                        "duration": "247000"
                    },
                    {
                        "number": "7",
                        "title": "I Know Places",
                        "duration": "195000"
                    },
                    {
                        "number": "8",
                        "title": "All You Had to Do Was Stay",
                        "duration": "193000"
                    },
                    {
                        "number": "9",
                        "title": "You Are in Love",
                        "duration": "492120"
                    },
                    {
                        "number": "10",
                        "title": "Clean",
                        "duration": "271000"
                    },
                    {
                        "number": "11",
                        "title": "Love Story",
                        "duration": "425000"
                    },
                    {
                        "number": "12",
                        "title": "Style",
                        "duration": "231000"
                    },
                    {
                        "number": "13",
                        "title": "This Love",
                        "duration": "250000"
                    },
                    {
                        "number": "14",
                        "title": "Bad Blood",
                        "duration": "211000"
                    },
                    {
                        "number": "15",
                        "title": "We Are Never Ever Getting Back Together",
                        "duration": "316000"
                    },
                    {
                        "number": "16",
                        "title": "Wildest Dreams",
                        "duration": "220000"
                    },
                    {
                        "number": "17",
                        "title": "Out of the Woods",
                        "duration": "235000"
                    },
                    {
                        "number": "18",
                        "title": "Shake It Off",
                        "duration": "219000"
                    }
                ]
            },
            {
                "id": "2284741",
                "title": "The Taylor Swift Megamix",
                "year": "2015",
                "genre": "Pop",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Opening",
                        "duration": "0"
                    },
                    {
                        "number": "2",
                        "title": "Shake It Off",
                        "duration": "0"
                    },
                    {
                        "number": "3",
                        "title": "Holy Ground",
                        "duration": "0"
                    },
                    {
                        "number": "4",
                        "title": "The Story Of Us",
                        "duration": "0"
                    },
                    {
                        "number": "5",
                        "title": "State Of Grace",
                        "duration": "0"
                    },
                    {
                        "number": "6",
                        "title": "You Belong With Me",
                        "duration": "0"
                    },
                    {
                        "number": "7",
                        "title": "Starlight",
                        "duration": "0"
                    },
                    {
                        "number": "8",
                        "title": "Red",
                        "duration": "0"
                    },
                    {
                        "number": "9",
                        "title": "New Romance",
                        "duration": "0"
                    },
                    {
                        "number": "10",
                        "title": "Mine",
                        "duration": "0"
                    },
                    {
                        "number": "11",
                        "title": "How You Get The Girl",
                        "duration": "0"
                    },
                    {
                        "number": "12",
                        "title": "Speak Now",
                        "duration": "0"
                    },
                    {
                        "number": "13",
                        "title": "Love Story",
                        "duration": "0"
                    },
                    {
                        "number": "14",
                        "title": "Welcome To New York",
                        "duration": "0"
                    },
                    {
                        "number": "15",
                        "title": "22",
                        "duration": "0"
                    },
                    {
                        "number": "16",
                        "title": "Long Live",
                        "duration": "0"
                    },
                    {
                        "number": "17",
                        "title": "Fearless",
                        "duration": "0"
                    },
                    {
                        "number": "18",
                        "title": "Teardrops On My Guitar",
                        "duration": "0"
                    },
                    {
                        "number": "19",
                        "title": "All You Had To Do Was Stay",
                        "duration": "0"
                    },
                    {
                        "number": "20",
                        "title": "Blank Space",
                        "duration": "0"
                    },
                    {
                        "number": "21",
                        "title": "Style",
                        "duration": "0"
                    },
                    {
                        "number": "22",
                        "title": "Fifteen",
                        "duration": "0"
                    },
                    {
                        "number": "23",
                        "title": "All Too Well",
                        "duration": "0"
                    },
                    {
                        "number": "24",
                        "title": "Our Song",
                        "duration": "0"
                    },
                    {
                        "number": "25",
                        "title": "We Are Never Ever Getting Back Together",
                        "duration": "0"
                    },
                    {
                        "number": "26",
                        "title": "Bad Blood",
                        "duration": "0"
                    },
                    {
                        "number": "27",
                        "title": "Shoud've Said No",
                        "duration": "0"
                    },
                    {
                        "number": "28",
                        "title": "Everything Has Changed",
                        "duration": "0"
                    },
                    {
                        "number": "29",
                        "title": "Begin Again",
                        "duration": "0"
                    },
                    {
                        "number": "30",
                        "title": "Today Was A Fairytale",
                        "duration": "0"
                    },
                    {
                        "number": "31",
                        "title": "I Knew You Were Trouble",
                        "duration": "0"
                    },
                    {
                        "number": "32",
                        "title": "Tim McGraw",
                        "duration": "0"
                    },
                    {
                        "number": "33",
                        "title": "I Almost Do",
                        "duration": "0"
                    },
                    {
                        "number": "34",
                        "title": "Back To December",
                        "duration": "0"
                    },
                    {
                        "number": "35",
                        "title": "Wildest Dreams",
                        "duration": "0"
                    },
                    {
                        "number": "36",
                        "title": "Eyes Open",
                        "duration": "0"
                    }
                ]
            },
            {
                "id": "2287637",
                "title": "\u2026Ready for It?",
                "year": "2017",
                "genre": "",
                "tracks": [
                    {
                        "number": "1",
                        "title": "\u2026Ready for It?",
                        "duration": "208224"
                    }
                ]
            },
            {
                "id": "2288123",
                "title": "reputation",
                "year": "2017",
                "genre": "Pop",
                "tracks": [
                    {
                        "number": "1",
                        "title": "\u2026Ready for It?",
                        "duration": "208000"
                    },
                    {
                        "number": "2",
                        "title": "End Game",
                        "duration": "244000"
                    },
                    {
                        "number": "3",
                        "title": "I Did Something Bad",
                        "duration": "238000"
                    },
                    {
                        "number": "4",
                        "title": "Don't Blame Me",
                        "duration": "236000"
                    },
                    {
                        "number": "5",
                        "title": "Delicate",
                        "duration": "232000"
                    },
                    {
                        "number": "6",
                        "title": "Look What You Made Me Do",
                        "duration": "211000"
                    },
                    {
                        "number": "7",
                        "title": "So It Goes\u2026",
                        "duration": "227000"
                    },
                    {
                        "number": "8",
                        "title": "Gorgeous",
                        "duration": "209000"
                    },
                    {
                        "number": "9",
                        "title": "Getaway Car",
                        "duration": "233000"
                    },
                    {
                        "number": "10",
                        "title": "King of My Heart",
                        "duration": "214000"
                    },
                    {
                        "number": "11",
                        "title": "Dancing with Our Hands Tied",
                        "duration": "211000"
                    },
                    {
                        "number": "12",
                        "title": "Dress",
                        "duration": "230000"
                    },
                    {
                        "number": "13",
                        "title": "This Is Why We Can't Have Nice Things",
                        "duration": "207000"
                    },
                    {
                        "number": "14",
                        "title": "Call It What You Want",
                        "duration": "203000"
                    },
                    {
                        "number": "15",
                        "title": "New Year's Day",
                        "duration": "235000"
                    }
                ]
            },
            {
                "id": "2327295",
                "title": "Lover",
                "year": "2019",
                "genre": "Pop",
                "tracks": [
                    {
                        "number": "1",
                        "title": "I Forgot That You Existed",
                        "duration": "170000"
                    },
                    {
                        "number": "2",
                        "title": "Cruel Summer",
                        "duration": "178000"
                    },
                    {
                        "number": "3",
                        "title": "Lover",
                        "duration": "221000"
                    },
                    {
                        "number": "4",
                        "title": "The Man",
                        "duration": "190000"
                    },
                    {
                        "number": "5",
                        "title": "The Archer",
                        "duration": "211000"
                    },
                    {
                        "number": "6",
                        "title": "I Think He Knows",
                        "duration": "173000"
                    },
                    {
                        "number": "7",
                        "title": "Miss Americana & the Heartbreak Prince",
                        "duration": "234000"
                    },
                    {
                        "number": "8",
                        "title": "Paper Rings",
                        "duration": "222000"
                    },
                    {
                        "number": "9",
                        "title": "Cornelia Street",
                        "duration": "287000"
                    },
                    {
                        "number": "10",
                        "title": "Death by a Thousand Cuts",
                        "duration": "198000"
                    },
                    {
                        "number": "11",
                        "title": "London Boy",
                        "duration": "190000"
                    },
                    {
                        "number": "12",
                        "title": "Soon You'll Get Better",
                        "duration": "201000"
                    },
                    {
                        "number": "13",
                        "title": "False God",
                        "duration": "200000"
                    },
                    {
                        "number": "14",
                        "title": "You Need to Calm Down",
                        "duration": "171000"
                    },
                    {
                        "number": "15",
                        "title": "Afterglow",
                        "duration": "223000"
                    },
                    {
                        "number": "16",
                        "title": "ME!",
                        "duration": "193000"
                    },
                    {
                        "number": "17",
                        "title": "It's Nice to Have a Friend",
                        "duration": "150000"
                    },
                    {
                        "number": "18",
                        "title": "Daylight",
                        "duration": "293000"
                    }
                ]
            },
            {
                "id": "2328402",
                "title": "Beautiful Eyes",
                "year": "2008",
                "genre": "Pop",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Beautiful Eyes",
                        "duration": "179160"
                    },
                    {
                        "number": "2",
                        "title": "Should\u2019ve Said No (alternate version)",
                        "duration": "226440"
                    },
                    {
                        "number": "3",
                        "title": "Teardrops on My Guitar (acoustic version)",
                        "duration": "178693"
                    },
                    {
                        "number": "4",
                        "title": "Picture to Burn (radio edit)",
                        "duration": "174213"
                    },
                    {
                        "number": "5",
                        "title": "I\u2019m Only Me When I\u2019m With You",
                        "duration": "214533"
                    },
                    {
                        "number": "6",
                        "title": "I Heart ?",
                        "duration": "195173"
                    },
                    {
                        "number": "1",
                        "title": "Beautiful Eyes",
                        "duration": "177000"
                    },
                    {
                        "number": "2",
                        "title": "Picture to Burn",
                        "duration": "217000"
                    },
                    {
                        "number": "3",
                        "title": "I\u2019m Only Me When I\u2019m With You",
                        "duration": "228000"
                    },
                    {
                        "number": "4",
                        "title": "\u201cTim McGraw\u201d Video",
                        "duration": "240000"
                    },
                    {
                        "number": "5",
                        "title": "Teardrops on My Guitar (pop version)",
                        "duration": "206000"
                    },
                    {
                        "number": "6",
                        "title": "Our Song",
                        "duration": "210000"
                    },
                    {
                        "number": "7",
                        "title": "Making of \"Picture to Burn\"",
                        "duration": "1324000"
                    },
                    {
                        "number": "8",
                        "title": "GAC New Artist Special",
                        "duration": "886000"
                    },
                    {
                        "number": "9",
                        "title": "Should\u2019ve Said No (2008 ACM Awards Performance)",
                        "duration": "244000"
                    }
                ]
            },
            {
                "id": "2337100",
                "title": "Greatest Hits",
                "year": "2015",
                "genre": '',
                "tracks": [
                    {
                        "number": "1",
                        "title": "Shake It Off",
                        "duration": "221200"
                    },
                    {
                        "number": "2",
                        "title": "Blank Space",
                        "duration": "233826"
                    },
                    {
                        "number": "3",
                        "title": "Style",
                        "duration": "233000"
                    },
                    {
                        "number": "4",
                        "title": "I Knew You Were Trouble",
                        "duration": "221720"
                    },
                    {
                        "number": "5",
                        "title": "We Are Never Ever Getting Back Together",
                        "duration": "195146"
                    },
                    {
                        "number": "6",
                        "title": "Begin Again",
                        "duration": "239613"
                    },
                    {
                        "number": "7",
                        "title": "Ours",
                        "duration": "241346"
                    },
                    {
                        "number": "8",
                        "title": "Mine",
                        "duration": "233706"
                    },
                    {
                        "number": "9",
                        "title": "Mean",
                        "duration": "240693"
                    },
                    {
                        "number": "10",
                        "title": "Sparks Fly",
                        "duration": "264920"
                    },
                    {
                        "number": "11",
                        "title": "Back to December (acoustic)",
                        "duration": "295946"
                    },
                    {
                        "number": "12",
                        "title": "Crazier",
                        "duration": "194946"
                    },
                    {
                        "number": "13",
                        "title": "Today Was a Fairytale",
                        "duration": "244626"
                    },
                    {
                        "number": "14",
                        "title": "Love Story",
                        "duration": "237440"
                    },
                    {
                        "number": "15",
                        "title": "You Belong With Me",
                        "duration": "234573"
                    },
                    {
                        "number": "16",
                        "title": "White Horse",
                        "duration": "237626"
                    },
                    {
                        "number": "17",
                        "title": "Change",
                        "duration": "282786"
                    },
                    {
                        "number": "18",
                        "title": "Should\u2019ve Said No",
                        "duration": "246080"
                    },
                    {
                        "number": "19",
                        "title": "Our Song (radio single version)",
                        "duration": "205440"
                    },
                    {
                        "number": "20",
                        "title": "Teardrops on My Guitar",
                        "duration": "204706"
                    },
                    {
                        "number": "1",
                        "title": "Bad Blood",
                        "duration": "202093"
                    },
                    {
                        "number": "2",
                        "title": "Welcome to New York",
                        "duration": "214600"
                    },
                    {
                        "number": "3",
                        "title": "Wildest Dreams",
                        "duration": "222440"
                    },
                    {
                        "number": "4",
                        "title": "State of Grace",
                        "duration": "297720"
                    },
                    {
                        "number": "5",
                        "title": "Red",
                        "duration": "225093"
                    },
                    {
                        "number": "6",
                        "title": "22",
                        "duration": "234120"
                    },
                    {
                        "number": "7",
                        "title": "Eyes Open",
                        "duration": "246586"
                    },
                    {
                        "number": "8",
                        "title": "Speak Now",
                        "duration": "245346"
                    },
                    {
                        "number": "9",
                        "title": "If This Was a Movie",
                        "duration": "238106"
                    },
                    {
                        "number": "10",
                        "title": "The Story of Us (US version)",
                        "duration": "267826"
                    },
                    {
                        "number": "11",
                        "title": "Jump Then Fall",
                        "duration": "240000"
                    },
                    {
                        "number": "12",
                        "title": "Beautiful Eyes",
                        "duration": "183040"
                    },
                    {
                        "number": "13",
                        "title": "You\u2019re Not Sorry",
                        "duration": "264813"
                    },
                    {
                        "number": "14",
                        "title": "Fearless",
                        "duration": "246506"
                    },
                    {
                        "number": "15",
                        "title": "Fifteen",
                        "duration": "298066"
                    },
                    {
                        "number": "16",
                        "title": "Forever & Always",
                        "duration": "228386"
                    },
                    {
                        "number": "17",
                        "title": "I\u2019m Only Me When I\u2019m With You",
                        "duration": "217600"
                    },
                    {
                        "number": "18",
                        "title": "Picture to Burn",
                        "duration": "177280"
                    },
                    {
                        "number": "19",
                        "title": "Tim McGraw",
                        "duration": "236546"
                    },
                    {
                        "number": "20",
                        "title": "Last Christmas",
                        "duration": "209693"
                    }
                ]
            },
            {
                "id": "2346607",
                "title": "folklore",
                "year": "2020",
                "genre": "Pop",
                "tracks": [
                    {
                        "number": "1",
                        "title": "the 1",
                        "duration": "210251"
                    },
                    {
                        "number": "2",
                        "title": "cardigan",
                        "duration": "239560"
                    },
                    {
                        "number": "3",
                        "title": "the last great american dynasty",
                        "duration": "230999"
                    },
                    {
                        "number": "4",
                        "title": "exile",
                        "duration": "285634"
                    },
                    {
                        "number": "5",
                        "title": "my tears ricochet",
                        "duration": "255893"
                    },
                    {
                        "number": "6",
                        "title": "mirrorball",
                        "duration": "208977"
                    },
                    {
                        "number": "7",
                        "title": "seven",
                        "duration": "208906"
                    },
                    {
                        "number": "8",
                        "title": "august",
                        "duration": "261922"
                    },
                    {
                        "number": "9",
                        "title": "this is me trying",
                        "duration": "195097"
                    },
                    {
                        "number": "10",
                        "title": "illicit affairs",
                        "duration": "190898"
                    },
                    {
                        "number": "11",
                        "title": "invisible string",
                        "duration": "252880"
                    },
                    {
                        "number": "12",
                        "title": "mad woman",
                        "duration": "237258"
                    },
                    {
                        "number": "13",
                        "title": "epiphany",
                        "duration": "289749"
                    },
                    {
                        "number": "14",
                        "title": "betty",
                        "duration": "294521"
                    },
                    {
                        "number": "15",
                        "title": "peace",
                        "duration": "234000"
                    },
                    {
                        "number": "16",
                        "title": "hoax",
                        "duration": "220042"
                    }
                ]
            },
            {
                "id": "2355516",
                "title": "evermore",
                "year": "2020",
                "genre": "Pop",
                "tracks": [
                    {
                        "number": "1",
                        "title": "willow",
                        "duration": "214000"
                    },
                    {
                        "number": "2",
                        "title": "champagne problems",
                        "duration": "244000"
                    },
                    {
                        "number": "3",
                        "title": "gold rush",
                        "duration": "185000"
                    },
                    {
                        "number": "4",
                        "title": "\u2018tis the damn season",
                        "duration": "229000"
                    },
                    {
                        "number": "5",
                        "title": "tolerate it",
                        "duration": "245000"
                    },
                    {
                        "number": "6",
                        "title": "no body, no crime",
                        "duration": "215000"
                    },
                    {
                        "number": "7",
                        "title": "happiness",
                        "duration": "315000"
                    },
                    {
                        "number": "8",
                        "title": "dorothea",
                        "duration": "225000"
                    },
                    {
                        "number": "9",
                        "title": "coney island",
                        "duration": "275000"
                    },
                    {
                        "number": "10",
                        "title": "ivy",
                        "duration": "260000"
                    },
                    {
                        "number": "11",
                        "title": "cowboy like me",
                        "duration": "275000"
                    },
                    {
                        "number": "12",
                        "title": "long story short",
                        "duration": "215000"
                    },
                    {
                        "number": "13",
                        "title": "marjorie",
                        "duration": "257000"
                    },
                    {
                        "number": "14",
                        "title": "closure",
                        "duration": "180000"
                    },
                    {
                        "number": "15",
                        "title": "evermore",
                        "duration": "304000"
                    }
                ]
            }
        ]
    },
    "Black Pumas": {
        "albums": [
            {
                "id": "2325985",
                "title": "Black Pumas",
                "year": "2019",
                "genre": '',
                "tracks": [
                    {
                        "number": "1",
                        "title": "Black Moon Rising",
                        "duration": "221947"
                    },
                    {
                        "number": "2",
                        "title": "Colors",
                        "duration": "246587"
                    },
                    {
                        "number": "3",
                        "title": "Know You Better",
                        "duration": "249920"
                    },
                    {
                        "number": "4",
                        "title": "Fire",
                        "duration": "246120"
                    },
                    {
                        "number": "5",
                        "title": "OCT 33",
                        "duration": "289707"
                    },
                    {
                        "number": "6",
                        "title": "Stay Gold",
                        "duration": "275333"
                    },
                    {
                        "number": "7",
                        "title": "Old Man",
                        "duration": "197053"
                    },
                    {
                        "number": "8",
                        "title": "Confines",
                        "duration": "189893"
                    },
                    {
                        "number": "9",
                        "title": "Touch The Sky",
                        "duration": "267440"
                    },
                    {
                        "number": "10",
                        "title": "Sweet Conversation",
                        "duration": "202600"
                    }
                ]
            }
        ]
    },
    "Black Eyed Peas": {
        "albums": [
            {
                "id": "2349011",
                "title": "Translation",
                "year": "2020",
                "genre": "Hip-Hop",
                "tracks": [
                    {
                        "number": "1",
                        "title": "RITMO (Bad Boys for Life)",
                        "duration": "214855"
                    },
                    {
                        "number": "2",
                        "title": "FEEL THE BEAT",
                        "duration": "237714"
                    },
                    {
                        "number": "3",
                        "title": "MAMACITA",
                        "duration": "251429"
                    },
                    {
                        "number": "4",
                        "title": "GIRL LIKE ME",
                        "duration": "222523"
                    },
                    {
                        "number": "5",
                        "title": "VIDA LOCA",
                        "duration": "234375"
                    },
                    {
                        "number": "6",
                        "title": "NO MA\u00d1ANA",
                        "duration": "221695"
                    },
                    {
                        "number": "7",
                        "title": "TONTA LOVE",
                        "duration": "230476"
                    },
                    {
                        "number": "8",
                        "title": "CELEBRATE",
                        "duration": "219813"
                    },
                    {
                        "number": "9",
                        "title": "TODO BUENO",
                        "duration": "230400"
                    },
                    {
                        "number": "10",
                        "title": "DURO HARD",
                        "duration": "205049"
                    },
                    {
                        "number": "11",
                        "title": "MABUTI",
                        "duration": "256000"
                    },
                    {
                        "number": "12",
                        "title": "I WOKE UP",
                        "duration": "210309"
                    },
                    {
                        "number": "13",
                        "title": "GET LOOSE NOW",
                        "duration": "147027"
                    },
                    {
                        "number": "14",
                        "title": "ACTION",
                        "duration": "252308"
                    },
                    {
                        "number": "15",
                        "title": "NEWS TODAY",
                        "duration": "256000"
                    },
                    {
                        "number": "16",
                        "title": "RITMO (Bad Boys For Life) (Remix)",
                        "duration": "229000"
                    },
                    {
                        "number": "17",
                        "title": "RITMO (Bad Boys For Life) (Steve Aoki Remix)",
                        "duration": "232000"
                    }
                ]
            }
        ]
    },
    "Arctic Monkeys": {
        "albums": [
            {
                "id": "2113919",
                "title": "Humbug",
                "year": "2009",
                "genre": "Indie",
                "tracks": [
                    {
                        "number": "1",
                        "title": "My Propeller",
                        "duration": "208000"
                    },
                    {
                        "number": "2",
                        "title": "Crying Lightning",
                        "duration": "223000"
                    },
                    {
                        "number": "3",
                        "title": "Dangerous Animals",
                        "duration": "211000"
                    },
                    {
                        "number": "4",
                        "title": "Secret Door",
                        "duration": "223000"
                    },
                    {
                        "number": "5",
                        "title": "Potion Approaching",
                        "duration": "212000"
                    },
                    {
                        "number": "6",
                        "title": "Fire and the Thud",
                        "duration": "238000"
                    },
                    {
                        "number": "7",
                        "title": "Cornerstone",
                        "duration": "198000"
                    },
                    {
                        "number": "8",
                        "title": "Dance Little Liar",
                        "duration": "283000"
                    },
                    {
                        "number": "9",
                        "title": "Pretty Visitors",
                        "duration": "221000"
                    },
                    {
                        "number": "10",
                        "title": "The Jeweller's Hands",
                        "duration": "342000"
                    },
                    {
                        "number": "11",
                        "title": "I Haven't Got My Strange",
                        "duration": "90000"
                    },
                    {
                        "number": "12",
                        "title": "Red Right Hand",
                        "duration": "260000"
                    }
                ]
            },
            {
                "id": "2113920",
                "title": "Whatever People Say I Am, That's What I'm Not",
                "year": "2006",
                "genre": "Indie",
                "tracks": [
                    {
                        "number": "1",
                        "title": "The View From the Afternoon",
                        "duration": "218000"
                    },
                    {
                        "number": "2",
                        "title": "I Bet You Look Good on the Dancefloor",
                        "duration": "173000"
                    },
                    {
                        "number": "3",
                        "title": "Fake Tales of San Francisco",
                        "duration": "178000"
                    },
                    {
                        "number": "4",
                        "title": "Dancing Shoes",
                        "duration": "141000"
                    },
                    {
                        "number": "5",
                        "title": "You Probably Couldn't See for the Lights but You Were Staring Straight at Me",
                        "duration": "130000"
                    },
                    {
                        "number": "6",
                        "title": "Still Take You Home",
                        "duration": "173000"
                    },
                    {
                        "number": "7",
                        "title": "Riot Van",
                        "duration": "135000"
                    },
                    {
                        "number": "8",
                        "title": "Red Light Indicates Doors Are Secured",
                        "duration": "143000"
                    },
                    {
                        "number": "9",
                        "title": "Mardy Bum",
                        "duration": "175000"
                    },
                    {
                        "number": "10",
                        "title": "Perhaps Vampires Is a Bit Strong But...",
                        "duration": "268000"
                    },
                    {
                        "number": "11",
                        "title": "When the Sun Goes Down",
                        "duration": "200000"
                    },
                    {
                        "number": "12",
                        "title": "From the Ritz to the Rubble",
                        "duration": "193000"
                    },
                    {
                        "number": "13",
                        "title": "A Certain Romance",
                        "duration": "331000"
                    }
                ]
            },
            {
                "id": "2113921",
                "title": "Favourite Worst Nightmare",
                "year": "2007",
                "genre": "Indie",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Brianstorm",
                        "duration": "170253"
                    },
                    {
                        "number": "2",
                        "title": "Teddy Picker",
                        "duration": "163146"
                    },
                    {
                        "number": "3",
                        "title": "D Is for Dangerous",
                        "duration": "136106"
                    },
                    {
                        "number": "4",
                        "title": "Balaclava",
                        "duration": "169226"
                    },
                    {
                        "number": "5",
                        "title": "Fluorescent Adolescent",
                        "duration": "177533"
                    },
                    {
                        "number": "6",
                        "title": "Only Ones Who Know",
                        "duration": "182760"
                    },
                    {
                        "number": "7",
                        "title": "Do Me a Favour",
                        "duration": "207253"
                    },
                    {
                        "number": "8",
                        "title": "This House Is a Circus",
                        "duration": "189680"
                    },
                    {
                        "number": "9",
                        "title": "If You Were There, Beware",
                        "duration": "274200"
                    },
                    {
                        "number": "10",
                        "title": "The Bad Thing",
                        "duration": "143213"
                    },
                    {
                        "number": "11",
                        "title": "Old Yellow Bricks",
                        "duration": "191226"
                    },
                    {
                        "number": "12",
                        "title": "505",
                        "duration": "253586"
                    }
                ]
            },
            {
                "id": "2113922",
                "title": "Suck It and See",
                "year": "2011",
                "genre": "Indie",
                "tracks": [
                    {
                        "number": "1",
                        "title": "She's Thunderstorms",
                        "duration": "234000"
                    },
                    {
                        "number": "2",
                        "title": "Black Treacle",
                        "duration": "215000"
                    },
                    {
                        "number": "3",
                        "title": "Brick by Brick",
                        "duration": "179000"
                    },
                    {
                        "number": "4",
                        "title": "The Hellcat Spangled Shalalala",
                        "duration": "180000"
                    },
                    {
                        "number": "5",
                        "title": "Don't Sit Down 'Cause I've Moved Your Chair",
                        "duration": "183000"
                    },
                    {
                        "number": "6",
                        "title": "Library Pictures",
                        "duration": "142000"
                    },
                    {
                        "number": "7",
                        "title": "All My Own Stunts",
                        "duration": "232000"
                    },
                    {
                        "number": "8",
                        "title": "Reckless Serenade",
                        "duration": "162000"
                    },
                    {
                        "number": "9",
                        "title": "Piledriver Waltz",
                        "duration": "203000"
                    },
                    {
                        "number": "10",
                        "title": "Love Is a Laserquest",
                        "duration": "191000"
                    },
                    {
                        "number": "11",
                        "title": "Suck It and See",
                        "duration": "226000"
                    },
                    {
                        "number": "12",
                        "title": "That's Where You're Wrong",
                        "duration": "256000"
                    },
                    {
                        "number": "13",
                        "title": "The Blond-O-Sonic Shimmer Trap",
                        "duration": "208000"
                    }
                ]
            },
            {
                "id": "2180196",
                "title": "AM",
                "year": "2013",
                "genre": "Indie",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Do I Wanna Know?",
                        "duration": "272000"
                    },
                    {
                        "number": "2",
                        "title": "R U Mine?",
                        "duration": "201000"
                    },
                    {
                        "number": "3",
                        "title": "One for the Road",
                        "duration": "206000"
                    },
                    {
                        "number": "4",
                        "title": "Arabella",
                        "duration": "207000"
                    },
                    {
                        "number": "5",
                        "title": "I Want It All",
                        "duration": "184000"
                    },
                    {
                        "number": "6",
                        "title": "No. 1 Party Anthem",
                        "duration": "243000"
                    },
                    {
                        "number": "7",
                        "title": "Mad Sounds",
                        "duration": "215000"
                    },
                    {
                        "number": "8",
                        "title": "Fireside",
                        "duration": "181000"
                    },
                    {
                        "number": "9",
                        "title": "Why'd You Only Call Me When You're High?",
                        "duration": "161000"
                    },
                    {
                        "number": "10",
                        "title": "Snap Out of It",
                        "duration": "192000"
                    },
                    {
                        "number": "11",
                        "title": "Knee Socks",
                        "duration": "257000"
                    },
                    {
                        "number": "12",
                        "title": "I Wanna Be Yours",
                        "duration": "184000"
                    }
                ]
            },
            {
                "id": "2193138",
                "title": "At the Apollo",
                "year": "2008",
                "genre": "Indie",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Brianstorm",
                        "duration": "182000"
                    },
                    {
                        "number": "2",
                        "title": "This House Is a Circus",
                        "duration": "193000"
                    },
                    {
                        "number": "3",
                        "title": "Teddy Picker",
                        "duration": "195000"
                    },
                    {
                        "number": "4",
                        "title": "I Bet You Look Good on the Dancefloor",
                        "duration": "172000"
                    },
                    {
                        "number": "5",
                        "title": "Dancing Shoes",
                        "duration": "170000"
                    },
                    {
                        "number": "6",
                        "title": "From the Ritz to the Rubble",
                        "duration": "203000"
                    },
                    {
                        "number": "7",
                        "title": "Fake Tales of San Francisco",
                        "duration": "176000"
                    },
                    {
                        "number": "8",
                        "title": "When the Sun Goes Down",
                        "duration": "214000"
                    },
                    {
                        "number": "9",
                        "title": "Nettles",
                        "duration": "189000"
                    },
                    {
                        "number": "10",
                        "title": "D Is for Dangerous",
                        "duration": "171000"
                    },
                    {
                        "number": "11",
                        "title": "Leave Before the Lights Come On",
                        "duration": "239000"
                    },
                    {
                        "number": "12",
                        "title": "Fluorescent Adolescent",
                        "duration": "199000"
                    },
                    {
                        "number": "13",
                        "title": "Still Take You Home",
                        "duration": "237000"
                    },
                    {
                        "number": "14",
                        "title": "Da Frame 2R",
                        "duration": "182000"
                    },
                    {
                        "number": "15",
                        "title": "Plastic Tramp",
                        "duration": "183000"
                    },
                    {
                        "number": "16",
                        "title": "505",
                        "duration": "304000"
                    },
                    {
                        "number": "17",
                        "title": "Do Me a Favour",
                        "duration": "208000"
                    },
                    {
                        "number": "18",
                        "title": "A Certain Romance",
                        "duration": "376000"
                    },
                    {
                        "number": "19",
                        "title": "The View From the Afternoon",
                        "duration": "223000"
                    },
                    {
                        "number": "20",
                        "title": "If You Were There, Beware",
                        "duration": "317000"
                    },
                    {
                        "number": "21",
                        "title": "Balaclava",
                        "duration": "159000"
                    },
                    {
                        "number": "22",
                        "title": "Bad Woman",
                        "duration": "176000"
                    },
                    {
                        "number": "1",
                        "title": "Riot Van",
                        "duration": "237000"
                    },
                    {
                        "number": "2",
                        "title": "The View From the Afternoon",
                        "duration": "235000"
                    },
                    {
                        "number": "3",
                        "title": "Still Take You Home",
                        "duration": "153000"
                    },
                    {
                        "number": "4",
                        "title": "You Probably Couldn't See for the Lights but You Were Staring Straight at Me",
                        "duration": "141000"
                    },
                    {
                        "number": "5",
                        "title": "Cigarette Smoker Fiona",
                        "duration": "178000"
                    },
                    {
                        "number": "6",
                        "title": "Perhaps Vampires Is a Bit Strong but...",
                        "duration": "235000"
                    },
                    {
                        "number": "7",
                        "title": "Dancing Shoes",
                        "duration": "170000"
                    },
                    {
                        "number": "8",
                        "title": "I Bet You Look Good on the Dancefloor",
                        "duration": "187000"
                    },
                    {
                        "number": "9",
                        "title": "When the Sun Goes Down",
                        "duration": "217000"
                    },
                    {
                        "number": "10",
                        "title": "A Certain Romance",
                        "duration": "406000"
                    }
                ]
            },
            {
                "id": "2197188",
                "title": "Who the Fuck Are Arctic Monkeys?",
                "year": "2006",
                "genre": "Indie",
                "tracks": [
                    {
                        "number": "1",
                        "title": "The View From the Afternoon",
                        "duration": "220946"
                    },
                    {
                        "number": "2",
                        "title": "Cigarette Smoker Fiona",
                        "duration": "176546"
                    },
                    {
                        "number": "3",
                        "title": "Despair in the Departure Lounge",
                        "duration": "202853"
                    },
                    {
                        "number": "4",
                        "title": "No Buses",
                        "duration": "197320"
                    },
                    {
                        "number": "5",
                        "title": "Who the Fuck Are Arctic Monkeys?",
                        "duration": "336826"
                    }
                ]
            },
            {
                "id": "2199566",
                "title": "Live in Texas: 7 June 2006",
                "year": "2006",
                "genre": "Indie",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Riot Van",
                        "duration": "0"
                    },
                    {
                        "number": "2",
                        "title": "The View From the Afternoon",
                        "duration": "0"
                    },
                    {
                        "number": "3",
                        "title": "Still Take You Home",
                        "duration": "0"
                    },
                    {
                        "number": "4",
                        "title": "You Probably Couldn't See for the Lights but You Were Staring Straight at Me",
                        "duration": "0"
                    },
                    {
                        "number": "5",
                        "title": "Cigarette Smoker Fiona",
                        "duration": "0"
                    },
                    {
                        "number": "6",
                        "title": "Perhaps Vampires Is a Bit Strong But...",
                        "duration": "0"
                    },
                    {
                        "number": "7",
                        "title": "Dancing Shoes",
                        "duration": "0"
                    },
                    {
                        "number": "8",
                        "title": "I Bet You Look Good on the Dancefloor",
                        "duration": "0"
                    },
                    {
                        "number": "9",
                        "title": "When the Sun Goes Down",
                        "duration": "0"
                    },
                    {
                        "number": "10",
                        "title": "A Certain Romance",
                        "duration": "0"
                    }
                ]
            },
            {
                "id": "2282924",
                "title": "The B-Sides",
                "year": "0",
                "genre": "Indie",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Bigger Boys and Stolen Sweethearts",
                        "duration": "178000"
                    },
                    {
                        "number": "2",
                        "title": "Chun Li's Spinning Bird Kick",
                        "duration": "280000"
                    },
                    {
                        "number": "3",
                        "title": "Stickin' to the Floor",
                        "duration": "79000"
                    },
                    {
                        "number": "4",
                        "title": "7",
                        "duration": "128000"
                    },
                    {
                        "number": "5",
                        "title": "Cigarette Smoke",
                        "duration": "176000"
                    },
                    {
                        "number": "6",
                        "title": "Despair in the Departure Lounge",
                        "duration": "202000"
                    },
                    {
                        "number": "7",
                        "title": "No Buses",
                        "duration": "197000"
                    },
                    {
                        "number": "8",
                        "title": "Who the Fuck Are Arctic Monkeys?",
                        "duration": "336000"
                    },
                    {
                        "number": "9",
                        "title": "Leave Before the Lights Come On",
                        "duration": "232000"
                    },
                    {
                        "number": "10",
                        "title": "Put Your Dukes Up John",
                        "duration": "182000"
                    },
                    {
                        "number": "11",
                        "title": "Baby I'm Yours",
                        "duration": "161000"
                    },
                    {
                        "number": "12",
                        "title": "If You Found This It's Probably Too Late",
                        "duration": "92000"
                    },
                    {
                        "number": "13",
                        "title": "Temptation Greets You Like Your Naughty Friend",
                        "duration": "207000"
                    },
                    {
                        "number": "14",
                        "title": "What If You Were Right the First Time?",
                        "duration": "182000"
                    },
                    {
                        "number": "15",
                        "title": "The Bakery",
                        "duration": "176000"
                    },
                    {
                        "number": "16",
                        "title": "Plastic Tramp",
                        "duration": "173000"
                    },
                    {
                        "number": "17",
                        "title": "Too Much to Ask",
                        "duration": "185000"
                    },
                    {
                        "number": "18",
                        "title": "Bad Woman",
                        "duration": "137000"
                    },
                    {
                        "number": "19",
                        "title": "The Death Ramps",
                        "duration": "199000"
                    },
                    {
                        "number": "20",
                        "title": "Nettles",
                        "duration": "105000"
                    }
                ]
            },
            {
                "id": "2302022",
                "title": "Tranquility Base Hotel + Casino",
                "year": "2018",
                "genre": "Indie",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Star Treatment",
                        "duration": "354000"
                    },
                    {
                        "number": "2",
                        "title": "One Point Perspective",
                        "duration": "208000"
                    },
                    {
                        "number": "3",
                        "title": "American Sports",
                        "duration": "158000"
                    },
                    {
                        "number": "4",
                        "title": "Tranquility Base Hotel + Casino",
                        "duration": "211000"
                    },
                    {
                        "number": "5",
                        "title": "Golden Trunks",
                        "duration": "173000"
                    },
                    {
                        "number": "6",
                        "title": "Four Out of Five",
                        "duration": "312000"
                    },
                    {
                        "number": "7",
                        "title": "The World's First Ever Monster Truck Front Flip",
                        "duration": "180000"
                    },
                    {
                        "number": "8",
                        "title": "Science Fiction",
                        "duration": "185000"
                    },
                    {
                        "number": "9",
                        "title": "She Looks Like Fun",
                        "duration": "182000"
                    },
                    {
                        "number": "10",
                        "title": "Batphone",
                        "duration": "271000"
                    },
                    {
                        "number": "11",
                        "title": "The Ultracheese",
                        "duration": "217000"
                    }
                ]
            },
            {
                "id": "2303432",
                "title": "iTunes Festival 2013",
                "year": "2014",
                "genre": "",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Do I Wanna Know?",
                        "duration": "0"
                    },
                    {
                        "number": "2",
                        "title": "Brianstorm",
                        "duration": "0"
                    },
                    {
                        "number": "3",
                        "title": "Dancing Shoes",
                        "duration": "0"
                    },
                    {
                        "number": "4",
                        "title": "Don't Sit Down Cause I've Moved Your Chair",
                        "duration": "0"
                    },
                    {
                        "number": "5",
                        "title": "Teddy Picker",
                        "duration": "0"
                    },
                    {
                        "number": "6",
                        "title": "Crying Lightning",
                        "duration": "0"
                    },
                    {
                        "number": "7",
                        "title": "Snap Out Of It",
                        "duration": "0"
                    },
                    {
                        "number": "8",
                        "title": "Brick By Brick",
                        "duration": "0"
                    },
                    {
                        "number": "9",
                        "title": "Old Yellow Brick",
                        "duration": "0"
                    },
                    {
                        "number": "10",
                        "title": "Fireside",
                        "duration": "0"
                    },
                    {
                        "number": "11",
                        "title": "Arabella",
                        "duration": "0"
                    },
                    {
                        "number": "12",
                        "title": "Pretty Visitors",
                        "duration": "0"
                    },
                    {
                        "number": "13",
                        "title": "I Bet You Look Good On The Dancefloor",
                        "duration": "0"
                    },
                    {
                        "number": "14",
                        "title": "One For The Road",
                        "duration": "0"
                    },
                    {
                        "number": "15",
                        "title": "Cornerstone",
                        "duration": "0"
                    },
                    {
                        "number": "16",
                        "title": "Fluorescent Adolescent",
                        "duration": "0"
                    },
                    {
                        "number": "17",
                        "title": "Why'd You Only Call Me You'r High?",
                        "duration": "0"
                    },
                    {
                        "number": "18",
                        "title": "R U Mine?",
                        "duration": "0"
                    },
                    {
                        "number": "19",
                        "title": "Suck It And See",
                        "duration": "0"
                    },
                    {
                        "number": "20",
                        "title": "505",
                        "duration": "0"
                    }
                ]
            },
            {
                "id": "2303433",
                "title": "Early B-Sides",
                "year": "2012",
                "genre": "",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Curtains Close",
                        "duration": "156626"
                    },
                    {
                        "number": "2",
                        "title": "Ravey Ravey Ravey Club",
                        "duration": "141346"
                    },
                    {
                        "number": "3",
                        "title": "On the Run From the MI5",
                        "duration": "103680"
                    },
                    {
                        "number": "4",
                        "title": "Knock a Door Run",
                        "duration": "264826"
                    },
                    {
                        "number": "5",
                        "title": "Stickin' to the Floor",
                        "duration": "112000"
                    },
                    {
                        "number": "6",
                        "title": "Choo Choo",
                        "duration": "188133"
                    },
                    {
                        "number": "7",
                        "title": "7",
                        "duration": "129937"
                    },
                    {
                        "number": "8",
                        "title": "Space Invader",
                        "duration": "166240"
                    },
                    {
                        "number": "9",
                        "title": "Settle for a Draw",
                        "duration": "195600"
                    },
                    {
                        "number": "10",
                        "title": "Wavin Bye to the Train or the Bus",
                        "duration": "183893"
                    }
                ]
            },
            {
                "id": "2303443",
                "title": "Underneath the Boardwalk",
                "year": "0",
                "genre": "",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Mardy Bum",
                        "duration": "175866"
                    },
                    {
                        "number": "2",
                        "title": "Still Take You Home",
                        "duration": "191986"
                    },
                    {
                        "number": "3",
                        "title": "Fake Tales of San Francisco",
                        "duration": "186213"
                    },
                    {
                        "number": "4",
                        "title": "A Certain Romance",
                        "duration": "326746"
                    },
                    {
                        "number": "5",
                        "title": "Dancing Shoes",
                        "duration": "147840"
                    },
                    {
                        "number": "6",
                        "title": "I Bet You Look Good on the Dancefloor",
                        "duration": "174613"
                    },
                    {
                        "number": "7",
                        "title": "Bigger Boys and Stolen Sweethearts",
                        "duration": "174346"
                    },
                    {
                        "number": "8",
                        "title": "Scummy",
                        "duration": "204813"
                    },
                    {
                        "number": "9",
                        "title": "Settle for a Draw - Live at the Forum",
                        "duration": "182546"
                    },
                    {
                        "number": "10",
                        "title": "Stickin' to the Floor - Live at the Forum",
                        "duration": "120546"
                    }
                ]
            },
            {
                "id": "2303444",
                "title": "2009-08-20: Kulturkirche, Cologne, Germany",
                "year": "2009",
                "genre": "",
                "tracks": [
                    {
                        "number": "1",
                        "title": "My Propeller",
                        "duration": "197000"
                    },
                    {
                        "number": "2",
                        "title": "Red Right Hand",
                        "duration": "264000"
                    },
                    {
                        "number": "3",
                        "title": "If You Were There, Beware",
                        "duration": "288000"
                    },
                    {
                        "number": "4",
                        "title": "Crying Lightning",
                        "duration": "266000"
                    },
                    {
                        "number": "5",
                        "title": "Potion Approaching",
                        "duration": "215000"
                    },
                    {
                        "number": "6",
                        "title": "Pretty Visitors",
                        "duration": "231000"
                    },
                    {
                        "number": "7",
                        "title": "Still Take You Home",
                        "duration": "183000"
                    },
                    {
                        "number": "8",
                        "title": "I Bet You Look Good on the Dancefloor",
                        "duration": "204000"
                    },
                    {
                        "number": "9",
                        "title": "Only Ones Who Know",
                        "duration": "203000"
                    },
                    {
                        "number": "10",
                        "title": "Brianstorm",
                        "duration": "195000"
                    },
                    {
                        "number": "11",
                        "title": "This House Is a Circus",
                        "duration": "248000"
                    },
                    {
                        "number": "12",
                        "title": "Dangerous Animals",
                        "duration": "217000"
                    },
                    {
                        "number": "13",
                        "title": "The View From the Afternoon",
                        "duration": "230000"
                    },
                    {
                        "number": "14",
                        "title": "Cornerstone",
                        "duration": "195000"
                    },
                    {
                        "number": "15",
                        "title": "Fluorescent Adolescent / Only You Know",
                        "duration": "250000"
                    },
                    {
                        "number": "16",
                        "title": "Secret Door",
                        "duration": "258000"
                    }
                ]
            },
            {
                "id": "2303445",
                "title": "2006-02-20: Black Session #243: Paris, France",
                "year": "2009",
                "genre": "",
                "tracks": [
                    {
                        "number": "1",
                        "title": "The View From the Afternoon",
                        "duration": "260000"
                    },
                    {
                        "number": "2",
                        "title": "I Bet You Look Good on the Dancefloor",
                        "duration": "180000"
                    },
                    {
                        "number": "3",
                        "title": "You Probably Couldn't See for the Lights but You Were Staring at Me",
                        "duration": "139000"
                    },
                    {
                        "number": "4",
                        "title": "Perhaps Vampires Is a Bit Strong But...",
                        "duration": "202000"
                    },
                    {
                        "number": "5",
                        "title": "From the Ritz to the Rubble",
                        "duration": "306000"
                    },
                    {
                        "number": "6",
                        "title": "When the Sun Goes Down",
                        "duration": "243000"
                    },
                    {
                        "number": "7",
                        "title": "Red Light Indicates Doors Are Secured",
                        "duration": "175000"
                    },
                    {
                        "number": "8",
                        "title": "Still Take You Home",
                        "duration": "198000"
                    },
                    {
                        "number": "9",
                        "title": "Dancing Shoes",
                        "duration": "178000"
                    },
                    {
                        "number": "10",
                        "title": "Bigger Boys and Stolen Sweethearts",
                        "duration": "192000"
                    },
                    {
                        "number": "11",
                        "title": "Mardy Bum",
                        "duration": "241000"
                    },
                    {
                        "number": "12",
                        "title": "Fake Tales of San Francisco",
                        "duration": "283000"
                    },
                    {
                        "number": "13",
                        "title": "A Certain Romance",
                        "duration": "404000"
                    }
                ]
            },
            {
                "id": "2303447",
                "title": "Radio Session",
                "year": "2007",
                "genre": "",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Teddy Picker",
                        "duration": "165000"
                    },
                    {
                        "number": "2",
                        "title": "Teddy Picker (clean version)",
                        "duration": "164000"
                    },
                    {
                        "number": "3",
                        "title": "Do Me a Favour",
                        "duration": "209000"
                    },
                    {
                        "number": "4",
                        "title": "Do Me a Favour (clean version)",
                        "duration": "208000"
                    },
                    {
                        "number": "5",
                        "title": "Brianstorm",
                        "duration": "183000"
                    },
                    {
                        "number": "6",
                        "title": "Balaclava",
                        "duration": "162000"
                    },
                    {
                        "number": "7",
                        "title": "Fluorescent Adolescent",
                        "duration": "185000"
                    }
                ]
            },
            {
                "id": "2303448",
                "title": "Beat 106 Session",
                "year": "2005",
                "genre": "",
                "tracks": [
                    {
                        "number": "1",
                        "title": "A Certain Romance",
                        "duration": "265000"
                    },
                    {
                        "number": "2",
                        "title": "Mardy Bum",
                        "duration": "171000"
                    },
                    {
                        "number": "3",
                        "title": "Riot Van",
                        "duration": "136000"
                    }
                ]
            },
            {
                "id": "2303450",
                "title": "Unreleased Tracks, Demos and Live",
                "year": "2006",
                "genre": "",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Space Invaders",
                        "duration": "165000"
                    },
                    {
                        "number": "2",
                        "title": "Curtains Closed",
                        "duration": "130000"
                    },
                    {
                        "number": "3",
                        "title": "Choo Choo",
                        "duration": "191000"
                    },
                    {
                        "number": "4",
                        "title": "Cigarette Smoke",
                        "duration": "178000"
                    },
                    {
                        "number": "5",
                        "title": "Wavin' Bye to the Train or the Bus",
                        "duration": "184000"
                    },
                    {
                        "number": "6",
                        "title": "I Bet You Look Good on the Dancefloor",
                        "duration": "178000"
                    },
                    {
                        "number": "7",
                        "title": "When the Sun Goes Down",
                        "duration": "207000"
                    },
                    {
                        "number": "8",
                        "title": "From the Ritz to the Rubble",
                        "duration": "187000"
                    },
                    {
                        "number": "9",
                        "title": "On the Run From the MI5",
                        "duration": "105000"
                    },
                    {
                        "number": "10",
                        "title": "Riot Van",
                        "duration": "135000"
                    }
                ]
            },
            {
                "id": "2303452",
                "title": "2006-01-29: BBC Radio 1: Jo Whiley's Live Lounge",
                "year": "0",
                "genre": "",
                "tracks": [
                    {
                        "number": "1",
                        "title": "I Bet You Look Good on the Dancefloor",
                        "duration": "165000"
                    },
                    {
                        "number": "2",
                        "title": "Love Machine",
                        "duration": "217000"
                    }
                ]
            },
            {
                "id": "2303453",
                "title": "The Soundtrack to 2006",
                "year": "2006",
                "genre": "",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Intro",
                        "duration": "43000"
                    },
                    {
                        "number": "2",
                        "title": "I Bet You Look Good on the Dance Floor",
                        "duration": "196000"
                    },
                    {
                        "number": "3",
                        "title": "The View From the Afternoon",
                        "duration": "139000"
                    },
                    {
                        "number": "4",
                        "title": "The View From the Afternoon (reprise)",
                        "duration": "105000"
                    },
                    {
                        "number": "5",
                        "title": "Still Take You Home",
                        "duration": "199000"
                    },
                    {
                        "number": "6",
                        "title": "You Probably Couldn't See for the Lights...",
                        "duration": "137000"
                    },
                    {
                        "number": "7",
                        "title": "Bigger Boys and Stolen Sweethearts",
                        "duration": "208000"
                    },
                    {
                        "number": "8",
                        "title": "Dancing Shoes",
                        "duration": "211000"
                    },
                    {
                        "number": "9",
                        "title": "When the Sun Goes Down (Scummy)",
                        "duration": "234000"
                    },
                    {
                        "number": "10",
                        "title": "From the Ritz to the Rubble",
                        "duration": "230000"
                    },
                    {
                        "number": "11",
                        "title": "Perhaps Vampires Is a Bit Strong But...",
                        "duration": "321000"
                    },
                    {
                        "number": "12",
                        "title": "Mardy Bum",
                        "duration": "222000"
                    },
                    {
                        "number": "13",
                        "title": "Fake Tales of San Francisco",
                        "duration": "242000"
                    },
                    {
                        "number": "14",
                        "title": "A Certain Romance",
                        "duration": "366000"
                    },
                    {
                        "number": "15",
                        "title": "The View From the Afternoon",
                        "duration": "209000"
                    },
                    {
                        "number": "16",
                        "title": "Dancing Shoes",
                        "duration": "154000"
                    },
                    {
                        "number": "17",
                        "title": "Fake Tales of San Francisco",
                        "duration": "183000"
                    },
                    {
                        "number": "18",
                        "title": "You Probably Couldn't See for the Lights...",
                        "duration": "134000"
                    },
                    {
                        "number": "19",
                        "title": "Perhaps Vampires Is a Bit Strong But...",
                        "duration": "273000"
                    },
                    {
                        "number": "20",
                        "title": "From the Ritz to the Rubble",
                        "duration": "210000"
                    },
                    {
                        "number": "21",
                        "title": "A Certain Romance",
                        "duration": "319000"
                    }
                ]
            },
            {
                "id": "2303455",
                "title": "Unplugged",
                "year": "2009",
                "genre": "",
                "tracks": [
                    {
                        "number": "1",
                        "title": "A Certain Romance",
                        "duration": "261000"
                    },
                    {
                        "number": "2",
                        "title": "Bigger Boys and Stolen Sweethearts",
                        "duration": "171000"
                    },
                    {
                        "number": "3",
                        "title": "Mardy Bum",
                        "duration": "167000"
                    },
                    {
                        "number": "4",
                        "title": "Riot Van",
                        "duration": "144000"
                    },
                    {
                        "number": "5",
                        "title": "No Buses",
                        "duration": "198000"
                    },
                    {
                        "number": "6",
                        "title": "The Bakery",
                        "duration": "159000"
                    },
                    {
                        "number": "7",
                        "title": "Fluorescent Adolescent",
                        "duration": "159000"
                    },
                    {
                        "number": "8",
                        "title": "Only Ones Who Know",
                        "duration": "139000"
                    },
                    {
                        "number": "9",
                        "title": "Too Much to Ask",
                        "duration": "128000"
                    },
                    {
                        "number": "10",
                        "title": "Crying Lightning",
                        "duration": "235000"
                    },
                    {
                        "number": "11",
                        "title": "Fire and the Thud",
                        "duration": "197000"
                    },
                    {
                        "number": "12",
                        "title": "Cornerstone",
                        "duration": "191000"
                    },
                    {
                        "number": "13",
                        "title": "Secret Door",
                        "duration": "234000"
                    },
                    {
                        "number": "14",
                        "title": "The Lovers",
                        "duration": "269000"
                    }
                ]
            },
            {
                "id": "2303457",
                "title": "Bigger Boys and Stolen Sweethearts",
                "year": "2006",
                "genre": "",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Bigger Boys and Stolen Sweethearts",
                        "duration": "174000"
                    },
                    {
                        "number": "2",
                        "title": "On the Run From the MI5",
                        "duration": "106000"
                    },
                    {
                        "number": "3",
                        "title": "Fake Tales of San Francisco",
                        "duration": "186000"
                    },
                    {
                        "number": "4",
                        "title": "I Bet You Look Good on the Dancefloor",
                        "duration": "110000"
                    },
                    {
                        "number": "5",
                        "title": "Choo Choo",
                        "duration": "190000"
                    },
                    {
                        "number": "6",
                        "title": "Ravey Ravey Ravey Club",
                        "duration": "144000"
                    },
                    {
                        "number": "7",
                        "title": "Mardy Bum",
                        "duration": "176000"
                    },
                    {
                        "number": "8",
                        "title": "Curtains Close",
                        "duration": "159000"
                    },
                    {
                        "number": "9",
                        "title": "Stickin' to the Floor",
                        "duration": "115000"
                    },
                    {
                        "number": "10",
                        "title": "A Certain Romance",
                        "duration": "327000"
                    },
                    {
                        "number": "11",
                        "title": "Dancing Shoes",
                        "duration": "148000"
                    },
                    {
                        "number": "12",
                        "title": "I Predict That You Look Good in a Riot",
                        "duration": "202000"
                    },
                    {
                        "number": "13",
                        "title": "Still Take You Home",
                        "duration": "192000"
                    },
                    {
                        "number": "14",
                        "title": "Riot Van",
                        "duration": "135000"
                    },
                    {
                        "number": "15",
                        "title": "No Buses (acoustic) (live)",
                        "duration": "196000"
                    },
                    {
                        "number": "16",
                        "title": "Wavin' Bye to the Train or the Bus",
                        "duration": "186000"
                    },
                    {
                        "number": "17",
                        "title": "Knock a Door Run",
                        "duration": "267000"
                    },
                    {
                        "number": "18",
                        "title": "Ravey Ravey Ravey Club (live, 2003-06-13: Sheffield)",
                        "duration": "140000"
                    },
                    {
                        "number": "19",
                        "title": "Space Invaders",
                        "duration": "168000"
                    },
                    {
                        "number": "20",
                        "title": "When the Sun Goes Down",
                        "duration": "205000"
                    },
                    {
                        "number": "21",
                        "title": "Cigarette Smoke",
                        "duration": "178000"
                    },
                    {
                        "number": "22",
                        "title": "Love Machine",
                        "duration": "198000"
                    },
                    {
                        "number": "23",
                        "title": "Scummy Justice (Drum n Bass remix)",
                        "duration": "864000"
                    }
                ]
            },
            {
                "id": "2310316",
                "title": "Brianstorm",
                "year": "2007",
                "genre": "Indie",
                "tracks": [
                    {
                        "number": "1",
                        "title": "If You Found This It's Probably Too Late",
                        "duration": "92373"
                    },
                    {
                        "number": "2",
                        "title": "Brianstorm",
                        "duration": "170866"
                    },
                    {
                        "number": "3",
                        "title": "Temptation Greets You Like Your Naughty Friend",
                        "duration": "207226"
                    },
                    {
                        "number": "4",
                        "title": "What If You Were Right the First Time?",
                        "duration": "182920"
                    }
                ]
            },
            {
                "id": "2318086",
                "title": "I Bet You Look Good on the Dancefloor",
                "year": "2005",
                "genre": "Indie Rock",
                "tracks": [
                    {
                        "number": "1",
                        "title": "I Bet You Look Good on the Dancefloor",
                        "duration": "174466"
                    },
                    {
                        "number": "2",
                        "title": "Bigger Boys and Stolen Sweethearts",
                        "duration": "178640"
                    },
                    {
                        "number": "3",
                        "title": "Chun Li\u2019s Spinning Bird Kick",
                        "duration": "280693"
                    }
                ]
            },
            {
                "id": "2358638",
                "title": "Why\u2019d You Only Call Me When You\u2019re High?",
                "year": "2013",
                "genre": '',
                "tracks": [
                    {
                        "number": "1",
                        "title": "Why\u2019d You Only Call Me When You\u2019re High?",
                        "duration": "161000"
                    },
                    {
                        "number": "2",
                        "title": "Stop the World I Wanna Get Off With You",
                        "duration": "191000"
                    }
                ]
            }
        ]
    },
    "Kanye West": {
        "albums": [
            {
                "id": "2114774",
                "title": "808s & Heartbreak",
                "year": "2008",
                "genre": "Hip-Hop",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Say You Will",
                        "duration": "378000"
                    },
                    {
                        "number": "2",
                        "title": "Welcome to Heartbreak",
                        "duration": "263000"
                    },
                    {
                        "number": "3",
                        "title": "Heartless",
                        "duration": "211000"
                    },
                    {
                        "number": "4",
                        "title": "Amazing",
                        "duration": "238000"
                    },
                    {
                        "number": "5",
                        "title": "Love Lockdown",
                        "duration": "270000"
                    },
                    {
                        "number": "6",
                        "title": "Paranoid",
                        "duration": "278000"
                    },
                    {
                        "number": "7",
                        "title": "RoboCop",
                        "duration": "274000"
                    },
                    {
                        "number": "8",
                        "title": "Street Lights",
                        "duration": "190000"
                    },
                    {
                        "number": "9",
                        "title": "Bad News",
                        "duration": "239000"
                    },
                    {
                        "number": "10",
                        "title": "See You in My Nightmares",
                        "duration": "258000"
                    },
                    {
                        "number": "11",
                        "title": "Coldest Winter",
                        "duration": "164000"
                    },
                    {
                        "number": "12",
                        "title": "Pinocchio Story (freestyle live from Singapore)",
                        "duration": "362000"
                    }
                ]
            },
            {
                "id": "2114784",
                "title": "My Beautiful Dark Twisted Fantasy",
                "year": "2010",
                "genre": "Hip-Hop",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Dark Fantasy",
                        "duration": "280000"
                    },
                    {
                        "number": "2",
                        "title": "Gorgeous",
                        "duration": "357000"
                    },
                    {
                        "number": "3",
                        "title": "Power",
                        "duration": "292000"
                    },
                    {
                        "number": "4",
                        "title": "All of the Lights (interlude)",
                        "duration": "62000"
                    },
                    {
                        "number": "5",
                        "title": "All of the Lights",
                        "duration": "299000"
                    },
                    {
                        "number": "6",
                        "title": "Monster",
                        "duration": "378000"
                    },
                    {
                        "number": "7",
                        "title": "So Appalled",
                        "duration": "398000"
                    },
                    {
                        "number": "8",
                        "title": "Devil in a New Dress",
                        "duration": "352000"
                    },
                    {
                        "number": "9",
                        "title": "Runaway",
                        "duration": "548000"
                    },
                    {
                        "number": "10",
                        "title": "Hell of a Life",
                        "duration": "327000"
                    },
                    {
                        "number": "11",
                        "title": "Blame Game",
                        "duration": "469000"
                    },
                    {
                        "number": "12",
                        "title": "Lost in the World",
                        "duration": "256000"
                    },
                    {
                        "number": "13",
                        "title": "Who Will Survive in America",
                        "duration": "98000"
                    }
                ]
            },
            {
                "id": "2114786",
                "title": "The College Dropout",
                "year": "2003",
                "genre": "Hip-Hop",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Intro",
                        "duration": "80000"
                    },
                    {
                        "number": "2",
                        "title": "Self Concious",
                        "duration": "226000"
                    },
                    {
                        "number": "3",
                        "title": "Jesus Walks (Intro)",
                        "duration": "52000"
                    },
                    {
                        "number": "4",
                        "title": "Jesus Walks",
                        "duration": "212000"
                    },
                    {
                        "number": "5",
                        "title": "Two Words",
                        "duration": "268000"
                    },
                    {
                        "number": "6",
                        "title": "The Good, the Bad, the Ugly",
                        "duration": "253000"
                    },
                    {
                        "number": "7",
                        "title": "Breathe In, Breathe Out",
                        "duration": "326000"
                    },
                    {
                        "number": "8",
                        "title": "Keep the Receipt",
                        "duration": "211000"
                    },
                    {
                        "number": "9",
                        "title": "Heavy Hitters",
                        "duration": "184000"
                    },
                    {
                        "number": "10",
                        "title": "Slow Jamz",
                        "duration": "300000"
                    },
                    {
                        "number": "11",
                        "title": "My Way",
                        "duration": "206000"
                    },
                    {
                        "number": "12",
                        "title": "Family Affair",
                        "duration": "281000"
                    },
                    {
                        "number": "13",
                        "title": "Through the Wire",
                        "duration": "277000"
                    },
                    {
                        "number": "14",
                        "title": "Never Let Me Down",
                        "duration": "272000"
                    },
                    {
                        "number": "15",
                        "title": "Home",
                        "duration": "245000"
                    },
                    {
                        "number": "16",
                        "title": "Through the Wire (remix)",
                        "duration": "140000"
                    },
                    {
                        "number": "17",
                        "title": "Wack Niggaz",
                        "duration": "105000"
                    },
                    {
                        "number": "18",
                        "title": "I Need to Know",
                        "duration": "145000"
                    }
                ]
            },
            {
                "id": "2114789",
                "title": "Graduation",
                "year": "2007",
                "genre": "Hip-Hop",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Good Morning",
                        "duration": "195000"
                    },
                    {
                        "number": "2",
                        "title": "Champion",
                        "duration": "168000"
                    },
                    {
                        "number": "3",
                        "title": "Stronger",
                        "duration": "312000"
                    },
                    {
                        "number": "4",
                        "title": "I Wonder",
                        "duration": "243000"
                    },
                    {
                        "number": "5",
                        "title": "Good Life",
                        "duration": "207000"
                    },
                    {
                        "number": "6",
                        "title": "Can't Tell Me Nothing",
                        "duration": "272000"
                    },
                    {
                        "number": "7",
                        "title": "Barry Bonds",
                        "duration": "204000"
                    },
                    {
                        "number": "8",
                        "title": "Drunk & Hot Girls",
                        "duration": "313000"
                    },
                    {
                        "number": "9",
                        "title": "Flashing Lights",
                        "duration": "238000"
                    },
                    {
                        "number": "10",
                        "title": "Everything I Am",
                        "duration": "228000"
                    },
                    {
                        "number": "11",
                        "title": "The Glory",
                        "duration": "213000"
                    },
                    {
                        "number": "12",
                        "title": "Homecoming",
                        "duration": "204000"
                    },
                    {
                        "number": "13",
                        "title": "Big Brother",
                        "duration": "588000"
                    },
                    {
                        "number": "14",
                        "title": "Good Night",
                        "duration": "186000"
                    },
                    {
                        "number": "15",
                        "title": "Bittersweet Poetry",
                        "duration": "394000"
                    }
                ]
            },
            {
                "id": "2163574",
                "title": "Late Registration",
                "year": "2005",
                "genre": "Hip-Hop",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Wake Up Mr. West",
                        "duration": "41000"
                    },
                    {
                        "number": "2",
                        "title": "Heard 'Em Say",
                        "duration": "203000"
                    },
                    {
                        "number": "3",
                        "title": "Touch the Sky",
                        "duration": "237000"
                    },
                    {
                        "number": "4",
                        "title": "Gold Digger",
                        "duration": "208000"
                    },
                    {
                        "number": "5",
                        "title": "Can't Afford No Gas (skit)",
                        "duration": "33000"
                    },
                    {
                        "number": "6",
                        "title": "Drive Slow",
                        "duration": "272000"
                    },
                    {
                        "number": "7",
                        "title": "My Way Home",
                        "duration": "103000"
                    },
                    {
                        "number": "8",
                        "title": "Crack Music",
                        "duration": "271000"
                    },
                    {
                        "number": "9",
                        "title": "Roses",
                        "duration": "245000"
                    },
                    {
                        "number": "10",
                        "title": "Bring Me Down",
                        "duration": "199000"
                    },
                    {
                        "number": "11",
                        "title": "Addiction",
                        "duration": "266000"
                    },
                    {
                        "number": "12",
                        "title": "We Broke (skit)",
                        "duration": "31000"
                    },
                    {
                        "number": "13",
                        "title": "Diamonds From Sierra Leone (remix)",
                        "duration": "233000"
                    },
                    {
                        "number": "14",
                        "title": "We Major",
                        "duration": "448000"
                    },
                    {
                        "number": "15",
                        "title": "Years Ago (skit)",
                        "duration": "24000"
                    },
                    {
                        "number": "16",
                        "title": "Hey Mama",
                        "duration": "305000"
                    },
                    {
                        "number": "17",
                        "title": "Celebration",
                        "duration": "198000"
                    },
                    {
                        "number": "18",
                        "title": "Imposter (skit)",
                        "duration": "78000"
                    },
                    {
                        "number": "19",
                        "title": "Gone",
                        "duration": "362000"
                    },
                    {
                        "number": "20",
                        "title": "Diamonds From Sierra Leone",
                        "duration": "304000"
                    },
                    {
                        "number": "21",
                        "title": "Back to Basics",
                        "duration": "99000"
                    },
                    {
                        "number": "22",
                        "title": "We Can Make It Better",
                        "duration": "232000"
                    },
                    {
                        "number": "23",
                        "title": "Late",
                        "duration": "230000"
                    }
                ]
            },
            {
                "id": "2173171",
                "title": "Yeezus",
                "year": "2013",
                "genre": "Hip-Hop",
                "tracks": [
                    {
                        "number": "1",
                        "title": "On Sight",
                        "duration": "156893"
                    },
                    {
                        "number": "2",
                        "title": "Black Skinhead",
                        "duration": "188306"
                    },
                    {
                        "number": "3",
                        "title": "I Am a God (feat. God)",
                        "duration": "231520"
                    },
                    {
                        "number": "4",
                        "title": "New Slaves",
                        "duration": "256093"
                    },
                    {
                        "number": "5",
                        "title": "Hold My Liquor",
                        "duration": "326946"
                    },
                    {
                        "number": "6",
                        "title": "I'm in It",
                        "duration": "234853"
                    },
                    {
                        "number": "7",
                        "title": "Blood on the Leaves",
                        "duration": "360280"
                    },
                    {
                        "number": "8",
                        "title": "Guilt Trip",
                        "duration": "243746"
                    },
                    {
                        "number": "9",
                        "title": "Send It Up",
                        "duration": "178040"
                    },
                    {
                        "number": "10",
                        "title": "Bound 2",
                        "duration": "229253"
                    }
                ]
            },
            {
                "id": "2212182",
                "title": "Mercy",
                "year": "2012",
                "genre": "Hip-Hop",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Mercy",
                        "duration": "332000"
                    }
                ]
            },
            {
                "id": "2218636",
                "title": "Christmas in Harlem",
                "year": "2010",
                "genre": "Hip-Hop",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Christmas in Harlem",
                        "duration": "236000"
                    }
                ]
            },
            {
                "id": "2237740",
                "title": "All Day",
                "year": "2015",
                "genre": "Hip-Hop",
                "tracks": [
                    {
                        "number": "1",
                        "title": "All Day",
                        "duration": "310000"
                    }
                ]
            },
            {
                "id": "2237741",
                "title": "Only One",
                "year": "2014",
                "genre": "Hip-Hop",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Only One",
                        "duration": "282000"
                    }
                ]
            },
            {
                "id": "2243960",
                "title": "G.O.O.D. Morning, G.O.O.D. Night",
                "year": "2009",
                "genre": "Hip-Hop",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Too Knight (The Underworld)",
                        "duration": "0"
                    },
                    {
                        "number": "2",
                        "title": "Chicago",
                        "duration": "0"
                    },
                    {
                        "number": "3",
                        "title": "Hit It Again",
                        "duration": "0"
                    },
                    {
                        "number": "4",
                        "title": "Know God",
                        "duration": "0"
                    },
                    {
                        "number": "5",
                        "title": "Magic Man",
                        "duration": "0"
                    },
                    {
                        "number": "6",
                        "title": "YUGO",
                        "duration": "0"
                    },
                    {
                        "number": "7",
                        "title": "My My",
                        "duration": "0"
                    },
                    {
                        "number": "8",
                        "title": "Waited",
                        "duration": "0"
                    },
                    {
                        "number": "9",
                        "title": "The Return (Here She Comes Again)",
                        "duration": "0"
                    },
                    {
                        "number": "10",
                        "title": "Da Slumz",
                        "duration": "0"
                    },
                    {
                        "number": "11",
                        "title": "Mean To Say",
                        "duration": "0"
                    },
                    {
                        "number": "12",
                        "title": "Addicted",
                        "duration": "0"
                    },
                    {
                        "number": "13",
                        "title": "Warpath",
                        "duration": "0"
                    },
                    {
                        "number": "14",
                        "title": "So Pop U Layer",
                        "duration": "0"
                    },
                    {
                        "number": "15",
                        "title": "Stop",
                        "duration": "0"
                    }
                ]
            },
            {
                "id": "2247774",
                "title": "Best of Kanye West",
                "year": "0",
                "genre": "Hip-Hop",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Girls, Girls Freestyle",
                        "duration": "214573"
                    },
                    {
                        "number": "2",
                        "title": "Tha' Bounce",
                        "duration": "260573"
                    },
                    {
                        "number": "3",
                        "title": "A Million Freestyle",
                        "duration": "79760"
                    },
                    {
                        "number": "4",
                        "title": "Home",
                        "duration": "244586"
                    },
                    {
                        "number": "5",
                        "title": "Whack Niggaz",
                        "duration": "105066"
                    },
                    {
                        "number": "6",
                        "title": "The Good, Bad, Ugly",
                        "duration": "138280"
                    },
                    {
                        "number": "7",
                        "title": "We are the Champions",
                        "duration": "356813"
                    },
                    {
                        "number": "8",
                        "title": "Playa, Playa freestyle",
                        "duration": "167866"
                    },
                    {
                        "number": "9",
                        "title": "Guess Who's Back",
                        "duration": "238560"
                    },
                    {
                        "number": "10",
                        "title": "My Way",
                        "duration": "204733"
                    },
                    {
                        "number": "11",
                        "title": "2 Words",
                        "duration": "176280"
                    },
                    {
                        "number": "12",
                        "title": "Love u Better Freestyle",
                        "duration": "107186"
                    },
                    {
                        "number": "13",
                        "title": "The Truth Freestyle",
                        "duration": "148906"
                    },
                    {
                        "number": "14",
                        "title": "Through the Wire",
                        "duration": "258814"
                    }
                ]
            },
            {
                "id": "2260051",
                "title": "The Life of Pablo",
                "year": "2016",
                "genre": "Hip-Hop",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Ultralight Beam",
                        "duration": "320000"
                    },
                    {
                        "number": "2",
                        "title": "Father Stretch My Hands Pt. 1",
                        "duration": "135000"
                    },
                    {
                        "number": "3",
                        "title": "Pt. 2",
                        "duration": "129000"
                    },
                    {
                        "number": "4",
                        "title": "Famous",
                        "duration": "194000"
                    },
                    {
                        "number": "5",
                        "title": "Feedback",
                        "duration": "155000"
                    },
                    {
                        "number": "6",
                        "title": "Low Lights",
                        "duration": "131000"
                    },
                    {
                        "number": "7",
                        "title": "Highlights",
                        "duration": "199000"
                    },
                    {
                        "number": "8",
                        "title": "Freestyle 4",
                        "duration": "122000"
                    },
                    {
                        "number": "9",
                        "title": "I Love Kanye",
                        "duration": "44000"
                    },
                    {
                        "number": "10",
                        "title": "Waves",
                        "duration": "181000"
                    },
                    {
                        "number": "11",
                        "title": "FML",
                        "duration": "236000"
                    },
                    {
                        "number": "12",
                        "title": "Real Friends",
                        "duration": "251000"
                    },
                    {
                        "number": "13",
                        "title": "Wolves",
                        "duration": "239000"
                    },
                    {
                        "number": "14",
                        "title": "Silver Surfer Intermission",
                        "duration": "56000"
                    },
                    {
                        "number": "15",
                        "title": "30 Hours",
                        "duration": "325000"
                    },
                    {
                        "number": "16",
                        "title": "No More Parties in LA",
                        "duration": "374000"
                    },
                    {
                        "number": "17",
                        "title": "Facts (Charlie Heat Version)",
                        "duration": "199000"
                    },
                    {
                        "number": "18",
                        "title": "Fade",
                        "duration": "193000"
                    }
                ]
            },
            {
                "id": "2262648",
                "title": "Classic (Better Than I've Ever Been)",
                "year": "2007",
                "genre": "",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Better Than I've Ever Been",
                        "duration": "246000"
                    },
                    {
                        "number": "2",
                        "title": "Better Than I've Ever Been (instrumental)",
                        "duration": "247000"
                    },
                    {
                        "number": "3",
                        "title": "Better Than I've Ever Been (a cappella)",
                        "duration": "223000"
                    },
                    {
                        "number": "4",
                        "title": "Classic (Better Than I've Ever Been) (DJ Premier remix)",
                        "duration": "282000"
                    },
                    {
                        "number": "5",
                        "title": "Classic (Better Than I've Ever Been) (DJ Premier remix) (instrumental)",
                        "duration": "282000"
                    }
                ]
            },
            {
                "id": "2268386",
                "title": "Champions",
                "year": "2016",
                "genre": "",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Champions",
                        "duration": "334000"
                    }
                ]
            },
            {
                "id": "2275423",
                "title": "College Dropout: Video Anthology",
                "year": "2005",
                "genre": "",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Through the Wire",
                        "duration": "0"
                    },
                    {
                        "number": "2",
                        "title": "Slow Jamz",
                        "duration": "0"
                    },
                    {
                        "number": "3",
                        "title": "All Falls Down",
                        "duration": "0"
                    },
                    {
                        "number": "4",
                        "title": "Two Words",
                        "duration": "0"
                    },
                    {
                        "number": "5",
                        "title": "The New Workout Plan (extended version)",
                        "duration": "0"
                    },
                    {
                        "number": "6",
                        "title": "Jesus Walks (Church version)",
                        "duration": "0"
                    },
                    {
                        "number": "7",
                        "title": "Jesus Walks (Chris Milk version)",
                        "duration": "0"
                    },
                    {
                        "number": "8",
                        "title": "Jesus Walks (Street version)",
                        "duration": "0"
                    },
                    {
                        "number": "9",
                        "title": "Get 'em High (instrumental version)",
                        "duration": "0"
                    },
                    {
                        "number": "1",
                        "title": "We Don't Care (reprise)",
                        "duration": "176893"
                    },
                    {
                        "number": "2",
                        "title": "Jesus Walks (remix)",
                        "duration": "298213"
                    },
                    {
                        "number": "3",
                        "title": "It's Alright",
                        "duration": "230733"
                    },
                    {
                        "number": "4",
                        "title": "The New Workout Plan (remix)",
                        "duration": "242026"
                    },
                    {
                        "number": "5",
                        "title": "Heavy Hitters",
                        "duration": "236386"
                    },
                    {
                        "number": "6",
                        "title": "Two Words (Cinematic)",
                        "duration": "246213"
                    },
                    {
                        "number": "7",
                        "title": "Never Let Me Down (Cinematic)",
                        "duration": "315534"
                    }
                ]
            },
            {
                "id": "2306985",
                "title": "ye",
                "year": "2018",
                "genre": "",
                "tracks": [
                    {
                        "number": "1",
                        "title": "I Thought About Killing You",
                        "duration": "273000"
                    },
                    {
                        "number": "2",
                        "title": "Yikes",
                        "duration": "191000"
                    },
                    {
                        "number": "3",
                        "title": "All Mine",
                        "duration": "147000"
                    },
                    {
                        "number": "4",
                        "title": "Wouldn't Leave",
                        "duration": "206000"
                    },
                    {
                        "number": "5",
                        "title": "No Mistakes",
                        "duration": "124000"
                    },
                    {
                        "number": "6",
                        "title": "Ghost Town",
                        "duration": "270000"
                    },
                    {
                        "number": "7",
                        "title": "Violent Crimes",
                        "duration": "214000"
                    }
                ]
            },
            {
                "id": "2309220",
                "title": "I Love It",
                "year": "2018",
                "genre": "",
                "tracks": [
                    {
                        "number": "1",
                        "title": "I Love It",
                        "duration": "127947"
                    }
                ]
            },
            {
                "id": "2315072",
                "title": "Late Orchestration",
                "year": "2006",
                "genre": "",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Diamonds from Sierra Leone",
                        "duration": "247853"
                    },
                    {
                        "number": "2",
                        "title": "Touch the Sky",
                        "duration": "246506"
                    },
                    {
                        "number": "3",
                        "title": "Crack Music",
                        "duration": "167853"
                    },
                    {
                        "number": "4",
                        "title": "Drive Slow",
                        "duration": "273760"
                    },
                    {
                        "number": "5",
                        "title": "Through the Wire",
                        "duration": "212773"
                    },
                    {
                        "number": "6",
                        "title": "Workout Plan",
                        "duration": "172840"
                    },
                    {
                        "number": "7",
                        "title": "Heard 'em Say",
                        "duration": "249600"
                    },
                    {
                        "number": "8",
                        "title": "All Falls Down",
                        "duration": "193280"
                    },
                    {
                        "number": "9",
                        "title": "Bring Me Down",
                        "duration": "200666"
                    },
                    {
                        "number": "10",
                        "title": "Gone",
                        "duration": "255186"
                    },
                    {
                        "number": "11",
                        "title": "Late",
                        "duration": "234186"
                    },
                    {
                        "number": "12",
                        "title": "Jesus Walks",
                        "duration": "193626"
                    },
                    {
                        "number": "13",
                        "title": "Gold Digger (AOL Sessions)",
                        "duration": "197960"
                    }
                ]
            },
            {
                "id": "2329820",
                "title": "Jesus is King",
                "year": "2019",
                "genre": "Hip-Hop",
                "tracks": [
                    {
                        "number": "1",
                        "title": "Every Hour",
                        "duration": "112000"
                    },
                    {
                        "number": "2",
                        "title": "Selah",
                        "duration": "164000"
                    },
                    {
                        "number": "3",
                        "title": "Follow God",
                        "duration": "104000"
                    },
                    {
                        "number": "4",
                        "title": "Closed On Sunday",
                        "duration": "151000"
                    },
                    {
                        "number": "5",
                        "title": "On God",
                        "duration": "136000"
                    },
                    {
                        "number": "6",
                        "title": "Everything We Need",
                        "duration": "116000"
                    },
                    {
                        "number": "7",
                        "title": "Water",
                        "duration": "168000"
                    },
                    {
                        "number": "8",
                        "title": "God Is",
                        "duration": "203000"
                    },
                    {
                        "number": "9",
                        "title": "Hands On",
                        "duration": "203000"
                    },
                    {
                        "number": "10",
                        "title": "Use This Gospel",
                        "duration": "213000"
                    },
                    {
                        "number": "11",
                        "title": "Jesus Is Lord",
                        "duration": "49000"
                    }
                ]
            }
        ]
    }
}