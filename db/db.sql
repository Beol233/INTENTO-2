-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema intento_2
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema intento_2
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `intento_2` DEFAULT CHARACTER SET utf8 ;
USE `intento_2` ;

-- -----------------------------------------------------
-- Table `intento_2`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `intento_2`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(255) NULL,
  `apellido` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `intento_2`.`viajes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `intento_2`.`viajes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `destino` VARCHAR(255) NULL,
  `fecha_inicio` DATETIME NULL,
  `fecha_fin` DATETIME NULL,
  `itinerario` TEXT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `intento_2`.`usuarios_has_viajes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `intento_2`.`usuarios_has_viajes` (
  `usuario_id` INT NOT NULL,
  `viaje_id` INT NOT NULL,
  PRIMARY KEY (`usuario_id`, `viaje_id`),
  INDEX `fk_usuarios_has_viajes_viajes1_idx` (`viaje_id` ASC) VISIBLE,
  INDEX `fk_usuarios_has_viajes_usuarios_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_usuarios_has_viajes_usuarios`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `intento_2`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_usuarios_has_viajes_viajes1`
    FOREIGN KEY (`viaje_id`)
    REFERENCES `intento_2`.`viajes` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
