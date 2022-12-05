import Link from "next/link";
import ThemeToggle from "./ThemeToggle";
import styles from '../../styles/Navbar.module.scss'

const Navbar = () => {
    return (
        <div className={styles.container}>
            <div className={styles.navigation}>
                <Link className={styles.link} href={'/'}>Main</Link>
                <Link className={styles.link} href={'/catalog'}>Catalog</Link>
                <Link className={styles.link} href={'/profile'}>Profile</Link>
            </div>
            <ThemeToggle/>
        </div>
    )
}

export default Navbar
