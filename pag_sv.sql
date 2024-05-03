-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 03, 2024 at 04:24 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pag_sv`
--

-- --------------------------------------------------------

--
-- Table structure for table `publicaciones`
--

CREATE TABLE `publicaciones` (
  `id` int(11) NOT NULL,
  `nombre_publicacion` varchar(255) NOT NULL,
  `descripcion` text NOT NULL,
  `ruta_imagen` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `publicaciones`
--

INSERT INTO `publicaciones` (`id`, `nombre_publicacion`, `descripcion`, `ruta_imagen`) VALUES
(1, 'Lago Moraine', 'Lago de montaña localizado en el Parque Nacional Banff, en Alberta, Canadá.', '1366_2000.jpg'),
(3, 'sunset on the lake', 'tal cual el titulo papu', 'AIx5.gif'),
(4, 'jotchua', 'Es jotchua con su amiguito', 'jotchua.jpg'),
(5, 'La pista', 'Carretera al Parque Nacional del Teide', 'HF_3_Paisajes_WEB-23.jpg'),
(6, 'Ambush Peak', 'Ambush Peak rises out the East Fork Valley as a jagged, distinct peak on the skyline.', 'fotografo-de-paisajes-naturales-del-ano-ganador-absoluto_5cbce102_800x533.jpg'),
(7, 'Luigi', 'Italian boy', 'FOTO_curriculum.png'),
(9, 'Calles de arequipa', 'Un pasaje del centro historico de Arequipa', 'c78307fb-city-10174-1732d430b8c.jpg'),
(10, 'Paisajin', 'un paisajin bonbin que se mueve', 'azulestrellla-imagenes-gif-34669294.gif'),
(11, 'Gojo ', 'Nah he\'d win', 'gojo na id win.jpg'),
(12, 'Animacion de cascada', 'awita que se mueve we', 'ff9979cbb47438d65c40c28aff16db09.gif'),
(14, 'otro paisajin', '100% real no fake paisaje 2024 mega mediafire', 'landscape-1192669_640.jpg'),
(15, ' Lago Esmeralda', 'Lago Emerald o lago Esmeralda situado en el Parque nacional Yoho, Canadá.', 'pexels-souvenirpixels-1619317.jpg'),
(16, 'El Misti', 'El volcán Misti en Arequipa', 'Volcano_Misti,_Peru.jpg'),
(17, 'Plaza de Armas', 'Plaza de Armas de la ciudad de Arequipa', 'plaza de armas arequipa.jpg'),
(20, 'Playa La Mina', 'Linda playa ubicada en Paracas', 'playa-la-mina.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(10) UNSIGNED NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `nom_comple` varchar(100) NOT NULL,
  `estado` int(1) NOT NULL,
  `rol` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `usuarios`
--

INSERT INTO `usuarios` (`id`, `username`, `password`, `nom_comple`, `estado`, `rol`) VALUES
(1, 'paquito', 'ppp', 'Alan Alvarez', 1, 1),
(4, 'toñito', 'ttt', 'Anthony Huicho', 0, 2),
(12, 'arianboi', 'aaa', 'Luigi Valenzuela', 1, 1),
(13, 'chago', 'ccc', 'Diego Hidalgo', 1, 2),
(16, 'gato', 'ggg', 'Sebastian Torres', 1, 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `publicaciones`
--
ALTER TABLE `publicaciones`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`),
  ADD KEY `rol` (`rol`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `publicaciones`
--
ALTER TABLE `publicaciones`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
