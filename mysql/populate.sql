use pokemon;
INSERT INTO `towns` (`townID`, `townName`, `population`) VALUES
(0, 'Pallet City', 34),
(1, 'Cerulian City', 55),
(2, 'Virdian City', 30),
(3, 'Pewter City',33),
(4, 'Vermillion City', 29),
(5, 'Lavender Town', 41),
(6, 'Celadon City', 82),
(7, 'Fuchsia City', 35),
(8,'Saffron City', 63),
(9, 'Cinnabar Island',36);

INSERT INTO `wild_pokemon` (`pID`, `pGender`, `pType`, `pName`) VALUES ('1', NULL, 'Grass', 'Bulbasaur'),
 ('2', NULL, 'Grass', 'Ivysaur'), ('3',NULL, 'Grass','Venasaur'), ('4',NULL,'Fire','Charmander'),
 ('5',NULL,'Fire','Charmeleon'),('6',NULL,'Fire','Charizard'), ('7',NULL,'Water','Squirtle'), 
 ('8',NULL, 'Water','Wartortle'), ('9',NULL, 'Water', 'Blastoise'), ('10',NULL, 'Bug','Caterpie'), 
 ('11',NULL, 'Bug','Metapod'), ('12', NULL, 'Bug', 'Butterfree'), ('13',NULL, 'Bug','Weedle'),
 ('14',NULL,'Bug','Kakuna'), ('15',NULL,'Bug','Beedrill'),('16',NULL,'Normal','Pidgey'),
 ('17',NULL,'Normal','Pigeotto'), ('18',NULL,'Normal','Pigeot'), ('19',NULL,'Normal','Rattata'),
 ('20',NULL,'Normal','Raticate'),('21',NULL,'Flying','Spearow'),('22',NULL,'Flying','Fearow'),
 ('23',NULL,'Posion','Ekans'),('24',NULL,'Posion','Arbok'),('25',NULL,'Thunder','Pikachu'),
 ('26',NULL,'Thunder','Raichu'),('27',NULL,'Ground','Sandshrew'),('28',NULL,'Ground','Sandslash'),
 ('29','F','Normal','Nidoran'),('30','F','Normal','Nidorina'),('31','F','Normal','Nidoqueen'),
 ('32','M','Normal','Nidoran'),('33','M','Normal','Nidorino'),('34','M','Normal','Nidoking'),
 ('35',NULL,'Normal','Clefairy'),('36',NULL,'Normal','Clefable'),('37',NULL,'Fire','Vulpix'),
 ('38',NULL,'Fire','Ninetales'),('39',NULL,'Normal','Jigglypuff'),('40',NULL,'Normal','Wigglytuff'),
 ('41',NULL,'Dark','Zubat'),('42',NULL,'Dark','Golbat'),('43',NULL,'Grass','Oddish'),
 ('44',NULL,'Grass','Gloom'),('45',NULL,'Grass','Vileplume')
 ;

INSERT INTO `trainers` (`tID`, `tName`, `tGender`, `towns_townID`, `numberOfPokemon`) VALUES
(NULL, 'Ash', 'M', 0, 0),
(NULL, 'Gary', 'M', 0, 0);

INSERT INTO `trainers` (`tID`, `tName`, `tGender`, `towns_townID`, `numberOfPokemon`) VALUES 
(NULL, 'Brock', 'M', '3', 0), 
(NULL, 'Misty', 'F', 1, 0),
(NULL, 'Lt. Surge', 'M', 4, 0)

;

INSERT INTO `gymleaders` (`gtID`, `gymName`, `type`, `badge`) VALUES (3, 'Rock Gym', 'Ground', 'Earth Badge'), 
(4, 'Water', 'Water', 'Water Badge');

INSERT INTO `wild_pokemon_found_in_towns` (`wild_pokemon_pID`, `towns_townID`) VALUES 
('1', '0'), ('1', '1'), (4,0),(7,0),(10,0),(10,1),(16,0),(16,1);



INSERT INTO `pokemon`.`trainers_battle_trainers` (`trainers_tID`, `trainers_tID1`, `winner`) VALUES ('1', '2', '1');


INSERT INTO `wild_pokemon_caught_by_trainers` (`pokemonID`, `wild_pokemon_pID`, `trainers_tID`, `pGender`, `pLevel`, `personalName`, `pokeHP`, `pokeHPMAX`) VALUES
(1, 1, 1, 'M', 1, 'Bulba',100,100),
(1, 1, 2, 'M', 4, 'Bulbasaur',100,100),
(2, 1, 1, 'M', 1, 'Bulba',100,100),
(3, 1, 1, 'F', 1, 'Bulby',100,100);


INSERT INTO `pokemon`.`items` (`itemID`, `itemName`, `itemDesc`) VALUES 
('1', 'potion', 'heals your pokemon 20 hit points'),
('2', 'super potion', 'heals your pokemon 40 hit points'),
('3', 'rare candy', 'advances your pokemon 1 level'),
('4', 'poke ball', 'used to catch pokemon'),
('5', 'great ball', 'more efficient than a poke ball'),
('6', 'master ball', 'guarenteed to catch a pokemon')
;

INSERT INTO `pokemon`.`trainers_has_items` (`itemNum`, `tID`, `items_itemID`) VALUES 
('1', '1', '1'),
('2','1','1'),
('3','1','4'),
('4','1','4'),
('5','1','4'),
('6','1','4'),
('1','2','1'),
('2','2','4')
;

