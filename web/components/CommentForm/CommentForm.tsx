import React, {ChangeEvent, FC, FormEvent, useContext, useState} from "react";
import css from "./CommentForm.module.css"
import {Comment, Post} from "../../types";
import {createComment} from "../../services";
import {currentUserContext, postContext} from "../PostPage/PostPage";
import {string} from "prop-types";
import {UserIcon} from "../UserIcon/UserIcon";

interface Props {
    parentID?: string;
    onSubmit: (text: Comment) => void;
    onCancel?: () => void;
}


export const CommentForm: FC<Props> = ({onSubmit, onCancel, parentID}) => {
    const [text, setText] = useState<string>('');
    const [error, setError] = useState<string>('');
    const [rows, setRows] = useState<number>(1 );
    const post = useContext(postContext)
    const currentUser = useContext(currentUserContext)

    const handleSubmit = async (evt: FormEvent<HTMLFormElement>) => {
        evt.preventDefault();
        let comment: Comment | undefined = undefined;
        try {
            comment = await createComment(post.id, text, parentID);
        } catch (e) {
            setError(e.toString());
            return
        }
        onSubmit(comment);
        setText('');
    };

    const handleTextChange = (evt: ChangeEvent<HTMLTextAreaElement>) => {
        setText(evt.currentTarget.value);
        const textareaLineHeight = 24;

        const previousRows = evt.target.rows;
  	    evt.target.rows = 1; // reset number of rows in textarea

        evt.target.rows = evt.target.rows + 1;
    }

    return (
        <form className={css.form} onSubmit={handleSubmit}>
                        <UserIcon user={currentUser} />
            <textarea
                rows={rows}
                className={css.input} value={text} onChange={handleTextChange}
            />
            <button type="submit" className={css.button}>
                Submit
            </button>
            {error && <p className={css.error}>{error}</p>}
        </form>
    );
}
