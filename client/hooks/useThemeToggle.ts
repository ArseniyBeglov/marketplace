import {useState, useEffect} from 'react'
import {useTheme} from "next-themes";

export const useThemeToggle = () => {
    const [mounted, setMounted] = useState<boolean>(false)
    const {theme, setTheme} = useTheme()

    useEffect(() => {
        setMounted(true)
    }, [])

    return {mounted, theme, setTheme}
}
