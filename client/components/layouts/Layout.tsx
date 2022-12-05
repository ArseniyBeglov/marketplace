import {FC, ReactElement} from "react";
import Navbar from "./Navbar";

interface IProps {
    children: ReactElement
}

const Layout:FC<IProps> = ({children}) => {
    return (
        <>
            <Navbar/>
            <div style={{margin: '0 20px'}}>
                {children}
            </div>
        </>
    )
}

export default Layout
