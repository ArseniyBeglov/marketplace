import '../styles/globals.scss'
import type {AppProps} from 'next/app'
import Layout from "../components/layouts/Layout";
import {ThemeProvider} from "next-themes";

export default function App({Component, pageProps}: AppProps) {
    return (
        <ThemeProvider attribute="class">
            <Layout>
                <Component {...pageProps} />
            </Layout>
        </ThemeProvider>
    )
}
