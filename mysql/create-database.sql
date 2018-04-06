-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema pokemon
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `pokemon` ;

-- -----------------------------------------------------
-- Schema pokemon
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `pokemon` DEFAULT CHARACTER SET utf8 ;
USE `pokemon` ;

-- -----------------------------------------------------
-- Table `pokemon`.`towns`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pokemon`.`towns` (
  `townID` INT(11) NOT NULL,
  `townName` VARCHAR(45) NOT NULL,
  `population` INT(11) NULL DEFAULT NULL,
  PRIMARY KEY (`townID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `pokemon`.`trainers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pokemon`.`trainers` (
  `tID` INT(11) NOT NULL AUTO_INCREMENT,
  `tName` VARCHAR(45) NOT NULL,
  `tGender` VARCHAR(45) NULL DEFAULT NULL,
  `towns_townID` INT(11) NOT NULL,
  `numberOfPokemon` INT NULL,
  PRIMARY KEY (`tID`),
  INDEX `fk_trainers_towns1_idx` (`towns_townID` ASC),
  CONSTRAINT `fk_trainers_towns1`
    FOREIGN KEY (`towns_townID`)
    REFERENCES `pokemon`.`towns` (`townID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `pokemon`.`badges`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pokemon`.`badges` (
  `tID` INT(11) NOT NULL,
  `badge` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`tID`, `badge`),
  CONSTRAINT `tID`
    FOREIGN KEY (`tID`)
    REFERENCES `pokemon`.`trainers` (`tID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `pokemon`.`gymleaders`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pokemon`.`gymleaders` (
  `gtID` INT(11) NOT NULL,
  `gymName` VARCHAR(45) NOT NULL,
  `type` VARCHAR(45) NOT NULL,
  `badge` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`gtID`),
  CONSTRAINT `gymID`
    FOREIGN KEY (`gtID`)
    REFERENCES `pokemon`.`trainers` (`tID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `pokemon`.`trainers_battle_trainers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pokemon`.`trainers_battle_trainers` (
  `battleID` INT(11) NOT NULL AUTO_INCREMENT,
  `trainers_tID` INT(11) NOT NULL,
  `trainers_tID1` INT(11) NOT NULL,
  `winner` INT(11) NOT NULL,
  PRIMARY KEY (`battleID`),
  UNIQUE INDEX `battleID_UNIQUE` (`battleID` ASC),
  INDEX `fk_trainers_has_trainers_trainers2_idx` (`trainers_tID1` ASC),
  INDEX `fk_trainers_has_trainers_trainers1_idx` (`trainers_tID` ASC),
  INDEX `winner_idx` (`winner` ASC),
  CONSTRAINT `fk_trainers_has_trainers_trainers1`
    FOREIGN KEY (`trainers_tID`)
    REFERENCES `pokemon`.`trainers` (`tID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_trainers_has_trainers_trainers2`
    FOREIGN KEY (`trainers_tID1`)
    REFERENCES `pokemon`.`trainers` (`tID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `winner`
    FOREIGN KEY (`winner`)
    REFERENCES `pokemon`.`trainers` (`tID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 3
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `pokemon`.`wild_pokemon`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pokemon`.`wild_pokemon` (
  `pID` INT(11) NOT NULL,
  `pGender` VARCHAR(45) NULL DEFAULT NULL,
  `pType` VARCHAR(45) NULL DEFAULT NULL,
  `pName` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`pID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `pokemon`.`items`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pokemon`.`items` (
  `itemID` INT NOT NULL,
  `itemName` VARCHAR(45) NOT NULL,
  `itemDesc` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`itemID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `pokemon`.`trainers_has_items`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pokemon`.`trainers_has_items` (
  `itemNum` INT NOT NULL,
  `tID` INT(11) NOT NULL,
  `items_itemID` INT NOT NULL,
  PRIMARY KEY (`itemNum`, `tID`),
  INDEX `fk_trainers_has_items_items1_idx` (`items_itemID` ASC),
  INDEX `fk_trainers_has_items_trainers1_idx` (`tID` ASC),
  CONSTRAINT `fk_tID`
    FOREIGN KEY (`tID`)
    REFERENCES `pokemon`.`trainers` (`tID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_trainers_has_items_items1`
    FOREIGN KEY (`items_itemID`)
    REFERENCES `pokemon`.`items` (`itemID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `pokemon`.`wild_pokemon_caught_by_trainers`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pokemon`.`wild_pokemon_caught_by_trainers` (
  `pokemonID` INT(11) NOT NULL,
  `wild_pokemon_pID` INT(11) NOT NULL,
  `trainers_tID` INT(11) NOT NULL,
  `pGender` VARCHAR(45) NOT NULL,
  `pLevel` INT(11) NOT NULL,
  `personalName` VARCHAR(45) NOT NULL,
  `pokeHP` INT NULL DEFAULT 100,
  `pokeHPMAX` INT NULL DEFAULT 100,
  `trainers_has_items_items_itemID` INT NULL,
  PRIMARY KEY (`pokemonID`, `wild_pokemon_pID`, `trainers_tID`),
  INDEX `fk_wild_pokemon_has_trainers_trainers1_idx` (`trainers_tID` ASC),
  INDEX `fk_wild_pokemon_has_trainers_wild_pokemon1_idx` (`wild_pokemon_pID` ASC),
  INDEX `fk_wild_pokemon_caught_by_trainers_trainers_has_items1_idx` (`trainers_has_items_items_itemID` ASC),
  CONSTRAINT `fk_wild_pokemon_has_trainers_trainers1`
    FOREIGN KEY (`trainers_tID`)
    REFERENCES `pokemon`.`trainers` (`tID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_wild_pokemon_has_trainers_wild_pokemon1`
    FOREIGN KEY (`wild_pokemon_pID`)
    REFERENCES `pokemon`.`wild_pokemon` (`pID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_wild_pokemon_caught_by_trainers_trainers_has_items1`
    FOREIGN KEY (`trainers_has_items_items_itemID`)
    REFERENCES `pokemon`.`trainers_has_items` (`items_itemID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `pokemon`.`wild_pokemon_found_in_towns`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `pokemon`.`wild_pokemon_found_in_towns` (
  `wild_pokemon_pID` INT(11) NOT NULL,
  `towns_townID` INT(11) NOT NULL,
  PRIMARY KEY (`wild_pokemon_pID`, `towns_townID`),
  INDEX `fk_wild_pokemon_has_towns_towns1_idx` (`towns_townID` ASC),
  INDEX `fk_wild_pokemon_has_towns_wild_pokemon1_idx` (`wild_pokemon_pID` ASC),
  CONSTRAINT `fk_wild_pokemon_has_towns_towns1`
    FOREIGN KEY (`towns_townID`)
    REFERENCES `pokemon`.`towns` (`townID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_wild_pokemon_has_towns_wild_pokemon1`
    FOREIGN KEY (`wild_pokemon_pID`)
    REFERENCES `pokemon`.`wild_pokemon` (`pID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
