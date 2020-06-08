import React, {ChangeEvent, FC, FormEvent, useContext, useState} from "react";
import css from "./CommentForm.module.css"
import {Comment, Post} from "../../types";
import {createComment} from "../../services";
import {postContext} from "../PostPage/PostPage";

interface Props {
    parentID?: string;
    onSubmit: (text: Comment) => void;
    onCancel?: () => void;
}


export const CommentForm: FC<Props> = ({onSubmit, onCancel, parentID}) => {
    const [text, setText] = useState<string>('');
    const [error, setError] = useState<string>('');
    const post = useContext(postContext)

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
    }
    return (
        <form className={css.form} onSubmit={handleSubmit}>
            <textarea className={css.input} value={text} onChange={handleTextChange}/>
            {error && <p className={css.error}>{error}</p>}
            <div className={css.buttons}>
                {onCancel && (
                    <button type="submit" onClick={onCancel}>
                        Cancel
                    </button>
                )}
                <button type="submit">
                    Submit
                </button>
            </div>
        </form>
    );
}
