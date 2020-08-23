import React, { ChangeEvent, FC, FormEvent, useContext, useEffect, useRef, useState } from "react";
import css from "./CommentForm.module.css"
import {Comment, Post, User} from "../../types";
import {createComment} from "../../services";
import {currentUserContext, postContext} from "../PostPage/PostPage";
import {UserIcon} from "../UserIcon/UserIcon";
import SendSVG from "./send.svg";
import autosize from "autosize";

interface Props {
    parentID?: string;
    onSubmit: (text: Comment) => void;
    onCancel?: () => void;
}

interface UserProps extends Props{
    currentUser: User;
}


export const CommentForm: FC<Props> = (props) => {
    const currentUser = useContext(currentUserContext)
    if (!currentUser) {
        return null
    }
    return <UserCommentForm {...props} currentUser={currentUser}/>;

};


export const UserCommentForm: FC<UserProps> = ({onSubmit, onCancel, parentID, currentUser}) => {
    const [text, setText] = useState<string>('');
    const [error, setError] = useState<string>('');
    const post = useContext(postContext);
    const textArea = useRef(null);

    useEffect(() => {
        textArea.current.focus();
        autosize(textArea.current);
    }, []);

    const handleSubmit = async (evt: FormEvent<HTMLFormElement>) => {
        evt.preventDefault();
        if (!text) {
            return; // nothing to submit
        }
        let comment: Comment | undefined = undefined;
        try {
            comment = await createComment(post.id, text, parentID);
        } catch (e) {
            setError(e.toString());
            return
        }
        onSubmit(comment);
        setText('');
        autosize.update(textArea.current);
    };

    const handleTextChange = (evt: ChangeEvent<HTMLTextAreaElement>) => {
        setText(evt.currentTarget.value);
    };

    return (
        <form className={css.form} onSubmit={handleSubmit}>
            <UserIcon user={currentUser} />
            <textarea
                className={css.input}
                rows={1}
                value={text}
                ref={textArea}
                onChange={handleTextChange}
                placeholder="Напишіть ваш коментар"
            />
            <button type="submit" className={css.button}>
                <SendSVG />
            </button>
            {error && <p className={css.error}>{error}</p>}
        </form>
    );
};
