import {useThemeToggle} from "../../hooks/useThemeToggle";
import styles from '../../styles/ThemeToggle.module.scss'

enum Themes {
    light = 'light',
    dark = 'dark'
}

const ThemeToggle = () => {

    const {mounted, theme, setTheme} = useThemeToggle()

    return (
        <div className={styles.container}>
            {mounted &&
                <button
                    className={styles.btn}
                    onClick={() => setTheme(theme === Themes.dark ? Themes.light : Themes.dark)}
                >
                </button>
            }
        </div>
    );
};

export default ThemeToggle;
