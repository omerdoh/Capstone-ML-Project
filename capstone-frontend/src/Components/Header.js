import React from 'react';
import styles from "../css/header.module.css"

const Header = () => {
  return (
    <header style={{ display: 'flex', position: 'fixed', top: 0, left: 0, width: '100%' }} className={styles.header}>
      <h3>Apollo AI Brand Recognition</h3>
      <nav>
        <ul>
          <a 
          style={{color:"white"}}
          href="https://www.algonquincollege.com/acmarketing/files/2020/01/ACGraphicStandards_January2020_RGB.pdf" 
          rel="noopener noreferrer"
          target="_blank"><h4 style={{color:"white", fontFamily:"Gotham"}}>Algonquin College Visual Identity Standards</h4></a>
        </ul>
      </nav>
    </header>
  );
}

export default Header;