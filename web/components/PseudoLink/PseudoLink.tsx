import React, {FC, MouseEventHandler} from "react";
import css from "./PseudoLink.module.css";

interface Props {
    onClick: (MouseEvent) => void;
}

const PseudoLink: FC<Props> = (props) => {
    const handleClick: MouseEventHandler<HTMLButtonElement> = (evt) => {
        evt.preventDefault();
        props.onClick(evt);
    }
    return <button className={css.link} onClick={handleClick}>{props.children}</button>
}

export default PseudoLink;